# Noto Backend

Backend en **FastAPI** para Noto: recibe un archivo de audio de una clase, lo transcribe con
AssemblyAI y genera notas estructuradas (títulos, resúmenes, action items, material de apoyo,
tareas) usando un modelo Qwen a través de un endpoint compatible con OpenAI (Alibaba Cloud).

Sigue una **Clean Architecture** por features: cada carpeta en `app/features/<nombre>/` se
divide en `domain` (reglas de negocio puras), `data` (implementaciones/IO) y `application`
(fábricas de casos de uso), todo independiente de la capa HTTP en `app/api/`.

> No hay `pyproject.toml` ni `requirements.txt` en el repo — las dependencias solo se pueden
> inferir de los imports: `fastapi`, `pydantic`, `pydantic-settings`, `supabase`, `PyJWT`,
> `assemblyai`, `openai`.

---

## 1. Estructura de carpetas

```
noto-backend/
├── .env                              # Variables de entorno (secretos — no se commitea)
├── app/
│   ├── main.py                       # Entry point de FastAPI + lifespan (clientes en app.state)
│   ├── test.py                       # Script manual de prueba (no es parte de la suite pytest)
│   │
│   ├── api/                          # Capa HTTP: routers, schemas y dependencias de FastAPI
│   │   ├── schemas/signin/signin_schemas.py   # SignInRequest
│   │   └── v1/
│   │       ├── signin/
│   │       │   ├── signin.py         # POST /signin/
│   │       │   └── deps.py           # Wiring de dependencias para el caso de uso de sign-in
│   │       └── notes/
│   │           ├── notes.py          # POST /notes/
│   │           └── deps.py           # Wiring de dependencias para el pipeline de notas
│   │
│   ├── core/
│   │   ├── config.py                 # `Settings` (pydantic-settings) — carga .env
│   │   ├── models.py                 # Listas de modelos de fallback (AssemblyAI / Qwen)
│   │   └── logging.py                # Configuración central de logging
│   │
│   ├── features/
│   │   ├── auth/                     # Feature de autenticación (sign-in) — ver §2
│   │   │   ├── domain/
│   │   │   ├── data/
│   │   │   └── application/
│   │   │
│   │   └── notes/                    # Feature de transcripción + generación de notas — ver §3
│   │       ├── domain/
│   │       │   ├── entities/transcript_entities.py   # TranscriptResult, Utterance, etc.
│   │       │   ├── entities/notes_entities.py         # NoteDraft, BlockDraft, BlockType
│   │       │   ├── repository/transcript.py           # TranscriptRepository (puerto)
│   │       │   ├── repository/notes_repository.py     # NotesRepository (puerto)
│   │       │   ├── usecases/notes_usecases.py         # TakeNotes
│   │       │   └── exceptions.py                      # UploadError, TranscriptError, AnalysisError
│   │       ├── data/
│   │       │   ├── datasource/transcript_datasource.py       # AssemblyAI (upload + transcribe)
│   │       │   ├── datasource/notes_datasource.py             # OpenAI-compatible (Qwen)
│   │       │   ├── datasource/note_persistence_datasource.py  # Supabase — pendiente de implementar
│   │       │   ├── models/transcript_models.py         # Modelos pydantic crudos de AssemblyAI
│   │       │   ├── models/notes_models.py               # Modelo pydantic de salida estructurada
│   │       │   ├── repository/transcript_repository_impl.py
│   │       │   └── repository/notes_repository_impl.py
│   │       └── application/
│   │           └── take_notes.py     # Fábrica del caso de uso + system prompt del modelo
│   │
│   └── tests/
│       └── test_transcript.py        # Desactualizado — ver §5
```

### 1.1 Cosas a tener en cuenta

- **`test.py` en la raíz de `app/`** es un script de desarrollo que se corre manualmente
  (`python -m app.test`), pega directo a la API de Alibaba y escribe el resultado en
  `note2.json`. No forma parte de la suite de pytest.
- **`app/tests/test_transcript.py` está desactualizado**: hace `monkeypatch` sobre
  `transcript_module.transcriber` y pega a `POST /transcript/`, pero ese atributo y esa ruta ya
  no existen — el endpoint actual es `POST /notes/` (`app/api/v1/notes/notes.py`) y el
  `transcriber` vive en `app.state`, no como global del módulo. Este test falla tal como está.
- **`note_persistence_datasource.py` no está implementado** (`save_transcript`/`save_notes` son
  `pass`) — por ahora las notas generadas no se persisten en Supabase, solo se devuelven en la
  respuesta HTTP.
- Los archivos `example.json`, `note.json`, `note2.json` en la raíz son salidas de prueba del
  script `test.py`, no artefactos del proyecto.

---

## 2. Feature: `auth` (sign-in)

Flujo: `router → deps.py (FastAPI) → application factory → usecase → repository (interfaz) →
repository impl → datasource → Supabase`.

- **`domain/entities/user.py`** — entidad `User` con validación en `__init__` y
  `from_json`/`to_json`.
- **`domain/exceptions.py`** — `InvalidCredentialsError`.
- **`domain/repository/sign_user_in.py`** — puerto abstracto `UserValidationRepository`.
- **`domain/usecases/sign_user.py`** — `SignUserIn.execute(email, password)`.
- **`data/datasource/sign_user_in_data_source.py`** — llama a
  `supabase_client.auth.sign_in_with_password(...)`.
- **`data/repository/sign_user_in_impl.py`** — traduce `AuthApiError` de Supabase a
  `InvalidCredentialsError` del dominio.
- **`application/sign_user_in.py`** — `create_sign_user_in_use_case(repository)`, sin
  dependencias de FastAPI (reusable fuera del contexto HTTP).
- **`api/v1/signin/deps.py`** — saca `supabase_admin` de `request.app.state` y arma la cadena.
- **`api/v1/signin/signin.py`** — `POST /signin/`, devuelve `{"access_token": ...}` o 401.

---

## 3. Feature: `notes` (transcripción + generación de notas)

Este es el corazón del backend. Flujo end-to-end de `POST /notes/`:

```
audio_bytes
  → TranscriptionDatasource (AssemblyAI: upload_file + transcribe)
  → TranscriptResultImpl._to_domain(...)      → TranscriptResult (dominio)
  → NotesDatasource.format_transcript(...)    → texto formateado en XML-like tags
  → OpenAI client (Qwen, structured output)   → NotesModel (pydantic)
  → NotesRepositoryImpl._to_domain(...)       → NoteDraft (dominio)
  → respuesta HTTP
```

### 3.1 Transcripción (`transcript_datasource.py`)

`TranscriptionDatasource` sube el audio a AssemblyAI (`upload_file`, corrido en un thread con
`asyncio.to_thread`) y luego llama a `transcribe(audio_url, config=...)`. La config
(`app.state.transcription_config`) pide modelos de voz en orden de fallback
(`core/models.py: ASSEMBLYAI_MODELS`), formateo de texto, puntuación y detección de idioma. Si
AssemblyAI responde `status == "error"`, se loguea y se lanza `ValueError`.

El resultado crudo (`TranscriptResultModel`) se traduce a la entidad de dominio
`TranscriptResult` en `TranscriptResultImpl._to_domain`, extrayendo `summary`, `action_items` y
`utterances` desde el bloque opcional `speech_understanding` de AssemblyAI.

### 3.2 Formateo del input para el modelo (`notes_datasource.py`)

`format_transcript` arma el texto que se le manda al modelo, incluyendo **solo** las secciones
que realmente vinieron en la transcripción (nada de tags vacíos):

- Si hay `summary` → bloque `<summary>...</summary>`.
- Si hay `action_items` → bloque `<action_items>...</action_items>`.
- Si hay `utterances` → bloque `<utterances>...</utterances>` (tiene prioridad sobre el texto
  plano).
- Si **no** hay `utterances` pero sí `text` → bloque `<transcript>...</transcript>` como
  fallback.

Las secciones se unen con un solo `\n`, sin líneas en blanco de más.

### 3.3 Selección de modelo y generación de notas

`select_model()` llama a `self._openai_client.models.list()` y elige el primer modelo
disponible de `alibaba_models` (fallback en orden, definido en `core/models.py:
ALIBABA_MODELS`). `create_note()` llama a
`self._openai_client.beta.chat.completions.parse(..., response_format=NotesModel)` con el
`system_prompt` de Noto (definido en `application/take_notes.py`), que le pide al modelo
generar notas completas y detalladas organizadas en bloques (`heading1-4`, `paragraph`,
`bullet_list_item`, `numbered_list_item`, `quote`, `callout`, `table`, `code`,
`todo_list_item`), con formato inline tipo Notion (`**bold**`, `` `highlight` ``,
`__underline__`) y sin inventar `homework`/`support_material` que no se mencionaron en clase.

`NotesModel` (pydantic, en `data/models/notes_models.py`) valida cada `Block`: limpia símbolos
de viñeta/numeración/emoji que el modelo haya puesto por error al inicio del texto
(`_LEADING_DECORATION_RE`), y solo permite `emoji` en los tipos de bloque que tiene sentido
(headings, table, callout).

### 3.4 Manejo de errores

- `TranscriptResultImpl` traduce cualquier excepción no controlada a `TranscriptError`.
- `NotesRepositoryImpl` traduce cualquier excepción no controlada a `AnalysisError`.
- El router (`notes.py`) captura `TranscriptError` y responde 422.

### 3.5 Wiring (`api/v1/notes/deps.py`)

`create_note(request)` arma toda la cadena leyendo del `app.state`:

```python
async def create_note(request: Request) -> TakeNotes:
    transcriber = request.app.state.transcriber
    transcription_config = request.app.state.transcription_config
    alibaba_client = request.app.state.alibaba_client
    alibaba_models = request.app.state.alibaba_models

    transcript_datasource = TranscriptionDatasource(transcriber, transcription_config)
    transcript_repository = TranscriptResultImpl(transcript_datasource)

    notes_datasource = NotesDatasource(alibaba_models=alibaba_models, openai_client=alibaba_client)
    notes_repository = NotesRepositoryImpl(notes_datasource)

    return create_take_notes_use_case(transcript_repository, notes_repository)
```

> Nota: antes `NotesDatasource` se instanciaba con `supabase_admin` en vez de `alibaba_client`
> en este mismo archivo, lo cual rompía en runtime (`'AsyncClient' object has no attribute
> 'models'`) porque el cliente de Supabase no tiene API de OpenAI. Ya está corregido.

---

## 4. `core/config.py` — Settings

Configuración tipada cargada desde `.env` vía `pydantic-settings`:

```python
class Settings(BaseSettings):
    ASSEMBLYAI_API_KEY: str
    ALIBABA_API_KEY: str
    ALIBABA_OPENAI_COMPATIBLE_ENDPOINT: str
    ALIBABA_DASHCOPE: str
    OPENROUTER_API_KEY: str
    ALIBABA_OSS_BUCKET: str
    ALIBABA_OSS_ENDPOINT: str
    ALIBABA_OSS_INTERNAL_ENDPOINT: str
    SUPABASE_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_JWS_URL: str
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
```

`core/models.py` define, por separado, las listas de modelos con fallback en orden:

```python
ASSEMBLYAI_MODELS = ["universal-2", "universal-3-pro", "universal-3-5-pro"]
ALIBABA_MODELS = ["qwen3.7-flash", "qwen3.5-flash"]
```

---

## 5. Logging (`core/logging.py`)

`setup_logging()` configura el logging raíz una sola vez, al importar `main.py`:

```python
def setup_logging() -> None:
    logging.basicConfig(
        level="DEBUG",
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        stream=sys.stdout,
    )
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
```

Cada módulo saca su logger con `logging.getLogger(__name__)`, así los logs quedan etiquetados
con el módulo exacto de origen (ya implementado en `notes_datasource.py` y
`transcript_datasource.py`, usando `logger.debug(...)` para el flujo normal y
`logger.exception(...)` dentro de los `except` para loguear el traceback completo).

**Cómo ver los logs:** al correr `uvicorn app.main:app --reload`, aparecen directo en la
terminal con el formato de arriba.

**Pendiente:** el campo `LOG_LEVEL` ya existe en `Settings` pero `setup_logging()` todavía tiene
el nivel *hardcodeado* a `"DEBUG"` en vez de leer `settings.LOG_LEVEL` — falta conectar ese
valor para poder controlar la verbosidad por variable de entorno.

Para bajar el ruido de librerías externas (por ejemplo, cada request HTTP que hace `httpx` al
subir el audio a AssemblyAI), se puede subir su nivel:

```python
logging.getLogger("httpx").setLevel(logging.WARNING)
```

---

## 6. `main.py` — Entry point

```python
setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.supabase_admin = await acreate_client(settings.SUPABASE_URL, settings.SUPABASE_API_KEY)
    app.state.jwks_client = PyJWKClient(settings.SUPABASE_JWS_URL)
    app.state.transcriber = Transcriber(api_key=settings.ASSEMBLYAI_API_KEY)
    app.state.transcription_config = TranscriptionConfig(
        speech_models=[*models.ASSEMBLYAI_MODELS],
        format_text=True,
        punctuate=True,
        language_detection=True,
    )
    app.state.alibaba_client = AsyncOpenAI(
        api_key=settings.ALIBABA_API_KEY,
        base_url=settings.ALIBABA_OPENAI_COMPATIBLE_ENDPOINT,
    )
    app.state.alibaba_models = models.ALIBABA_MODELS
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(signin_router, prefix="")
app.include_router(transcript_router, prefix="")
```

En el startup se crean: el cliente admin de Supabase, un `PyJWKClient` para verificar JWTs de
Supabase, el `Transcriber` y su `TranscriptionConfig` de AssemblyAI, y el cliente
`AsyncOpenAI` apuntando al endpoint compatible de Alibaba (Qwen). Todos quedan en `app.state`
para que las funciones de `deps.py` de cada feature los recojan por request.

---

## 7. Endpoints

| Método | Ruta        | Descripción                                                      |
|--------|-------------|-------------------------------------------------------------------|
| POST   | `/signin/`  | Autentica contra Supabase, devuelve `access_token`.               |
| POST   | `/notes/`   | Recibe `audio_file` (multipart), transcribe y genera notas.       |
| GET    | `/`         | Health check trivial (`{"message": "Hello, World!"}`).            |

---

## 8. Pendientes conocidos

- Conectar `settings.LOG_LEVEL` a `setup_logging()` (ver §5).
- Implementar `NotePersistentDatasource.save_transcript` / `save_notes` (persistencia en
  Supabase — actualmente son no-ops).
- Actualizar o eliminar `app/tests/test_transcript.py`, que apunta a una ruta y un atributo que
  ya no existen.
- Decidir qué hacer con `app/test.py` y los JSON de prueba sueltos en la raíz
  (`example.json`, `note.json`, `note2.json`) — son artefactos de desarrollo manual.
