# Noto Backend — Project Structure

FastAPI backend using a feature-based **Clean Architecture** layout: each feature under
`app/features/<name>/` is split into `domain` (business rules), `data` (implementations/IO),
and `application` (wiring/use-case factories), independent of the HTTP layer in `app/api/`.

> No `pyproject.toml` / `requirements.txt` was found in this repo — dependencies are currently
> only inferable from imports (fastapi, pydantic, pydantic-settings, supabase, PyJWT, assemblyai).

---

## 1. Folder Structure

```
noto-backend/
├── .env                          # Environment variables (secrets — not committed)
├── app/
│   ├── __init__.py                # Empty, marks app/ as a package
│   ├── main.py                    # FastAPI app entrypoint + lifespan (Supabase/JWKS client setup)
│   │
│   ├── api/                       # HTTP layer: routers & request/response schemas
│   │   ├── __init__.py            # Empty
│   │   ├── schemas/
│   │   │   └── signin/
│   │   │       └── signin_schemas.py   # SignInRequest pydantic model
│   │   └── v1/
│   │       ├── signin/
│   │       │   └── signin.py      # /signin/ router — the one actually mounted in main.py
│   │       └── transcript/
│   │           └── transcript.py  # Dead code: duplicate /signin/ route (unmounted) + a fully
│   │                               # commented-out /transcript/ endpoint and its AssemblyAI logic
│   │
│   ├── core/
│   │   ├── __init__.py            # Empty
│   │   └── config.py              # `Settings` (pydantic-settings) — loads .env into typed fields
│   │
│   ├── features/
│   │   └── auth/                  # The only fully-implemented feature — see §2
│   │       ├── domain/
│   │       │   ├── entities/user.py
│   │       │   ├── exceptions.py
│   │       │   ├── repository/sign_user_in.py
│   │       │   └── usecases/sign_user.py
│   │       ├── data/
│   │       │   ├── datasource/sign_user_in_data_source.py
│   │       │   └── repository/sign_user_in_impl.py
│   │       └── application/
│   │           └── sign_user_in.py
│   │
│   └── tests/
│       ├── __init__.py            # Empty
│       └── test_transcript.py     # Test for the (currently disabled) /transcript/ endpoint
```

### 1.1 Things worth knowing while reading this

- **Two `/signin/` routers exist.** `main.py` mounts `signin_router` from
  `app/api/v1/signin/signin.py`. `app/api/v1/transcript/transcript.py` still defines its own
  duplicate `/signin/` route and `SignInRequest` inline — it's unmounted dead code at this
  point, kept alive only by `test_transcript.py` which imports the module.
- **`/transcript/` is fully commented out** in `transcript.py` (upload/transcribe helpers and
  the route itself), so `test_transcript.py` will fail against the current router — it's a
  spec for a not-yet-wired feature.
- **`.env` contains live secrets** (AssemblyAI, Alibaba, Supabase keys) — it's gitignored;
  never commit it.

---

## 2. Feature: `auth` (sign-in)

The only feature implemented end-to-end across all three layers. Flow:

`api router → application factory → domain usecase → domain repository (interface) → data repository (impl) → data datasource → Supabase`

### 2.1 Domain layer (`app/features/auth/domain/`)

Pure business rules — no FastAPI, no Supabase SDK imports.

**`entities/user.py`** — `User` entity with validation in `__init__` (name/last_name/nickname
can't be empty), equality/hash by `user_id`, and `from_json`/`to_json` (de)serialization:

```python
class User:
    def __init__(self, user_id: str, nickname: str, name: str, last_name: str, credits: float = 0.0):
        if not name.strip():
            raise ValueError("name cannot be empty")
        ...
    @classmethod
    def from_json(cls, data: dict) -> "User": ...
    def to_json(self) -> dict: ...
```

**`exceptions.py`** — domain-level error hierarchy:

```python
class DomainError(Exception):
    """Base class for all domain-level errors."""

class InvalidCredentialsError(DomainError):
    """Raised when sign-in credentials don't match any user."""
```

**`repository/sign_user_in.py`** — abstract port the domain depends on (implemented in the
data layer, per the Dependency Inversion Principle):

```python
class UserValidationRepository(ABC):
    @abstractmethod
    async def sign_in_jwt(self, email: str, password: str) -> str:
        "Authenticates a user and returns access token"
```

**`usecases/sign_user.py`** — `SignUserIn` orchestrates the sign-in through the abstract
repository:

```python
class SignUserIn:
    def __init__(self, validationRepository: UserValidationRepository):
        self.validationRepository = validationRepository

    async def execute(self, email: str, password: str):
        try:
            return await self.validationRepository.sign_in_jwt(email=email, password=password)
        except InvalidCredentialsError:
            raise
```

### 2.2 Data layer (`app/features/auth/data/`)

Concrete implementations that talk to Supabase.

**`datasource/sign_user_in_data_source.py`** — lowest-level wrapper around the Supabase
Python SDK's auth call:

```python
class UserValidationDatasource:
    def __init__(self, client: AsyncClient):
        self._client = client

    async def sign_in_with_password(self, email: str, password: str) -> str:
        response = await self._client.auth.sign_in_with_password({
            "email": email, "password": password,
        })
        return response.session.access_token
```

**`repository/sign_user_in_impl.py`** — implements the domain's `UserValidationRepository`,
translating Supabase's `AuthApiError` into the domain's `InvalidCredentialsError`:

```python
class UserValidationRepositoryImpl(UserValidationRepository):
    def __init__(self, datasource: UserValidationDatasource):
        self._datasource = datasource

    async def sign_in_jwt(self, email: str, password: str) -> str:
        try:
            access_token = await self._datasource.sign_in_with_password(email, password)
            return access_token
        except AuthApiError as e:
            raise InvalidCredentialsError("Invalid email or password") from e
```

### 2.3 Application layer (`app/features/auth/application/`)

**`sign_user_in.py`** — a FastAPI-dependency factory that wires the concrete datasource →
repository → usecase chain per-request, pulling the shared Supabase admin client off
`app.state` (set up in `main.py`'s lifespan):

```python
def get_sign_user_in_use_case(request: Request) -> SignUserIn:
    datasource = UserValidationDatasource(request.app.state.supabase_admin)
    repository = UserValidationRepositoryImpl(datasource)
    return SignUserIn(repository)
```

### 2.4 API layer (`app/api/`)

**`schemas/signin/signin_schemas.py`** — request body contract:

```python
class SignInRequest(BaseModel):
    email: str = Field(..., min_length=3)
    password: str = Field(..., min_length=3)
```

**`v1/signin/signin.py`** — the dedicated router, and the one `main.py` mounts:

```python
signin_router = APIRouter()

@signin_router.post("/signin/")
async def signin(body: SignInRequest, use_case: SignUserIn = Depends(get_sign_user_in_use_case)):
    try:
        token = await use_case.execute(email=body.email, password=body.password)
        return {"access_token": token}
    except InvalidCredentialsError:
        raise HTTPException(401, "Invalid email or password")
```

**`v1/transcript/transcript.py`** — not mounted anywhere; contains a duplicate inline
`/signin/` route (rather than importing the one above) plus a disabled `/transcript/`
endpoint and its AssemblyAI upload/transcribe helpers, all commented out.

---

## 3. `core/config.py` — Settings

Typed environment configuration loaded via `pydantic-settings`:

```python
class Settings(BaseSettings):
    ASSEMBLYAI_API_KEY: str = Field(default="", description="AssemblyAI API Key")
    ALIBABA_API_KEY: str = Field(default="", description="Alibaba API Key")
    ALIBABA_OSS_BUCKET: str = Field(default="", description="Alibaba OSS Bucket Name")
    ALIBABA_OSS_ENDPOINT: str = Field(default="", description="Alibaba OSS Endpoint")
    ALIBABA_OSS_INTERNAL_ENDPOINT: str = Field(default="", description="Alibaba OSS Internal Endpoint")
    SUPABASE_API_KEY: str = Field(default="", description="Supabase API Key")
    SUPABASE_URL: str = Field(default="", description="Supabase URL")
    SUPABASE_JWS_URL: str = Field(default="", description="Supabase JWS URL")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
```

`main.py` consumes `SUPABASE_URL`, `SUPABASE_API_KEY`, `SUPABASE_JWS_URL`, and
`ASSEMBLYAI_API_KEY` from here — all fields it uses now exist on `Settings`.

---

## 4. `main.py` — App entrypoint

```python
from assemblyai import Transcriber
from app.core.config import settings
from fastapi import FastAPI
from jwt import PyJWKClient
from supabase import acreate_client
from app.api.v1.signin.signin import signin_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.supabase_admin = await acreate_client(
        settings.SUPABASE_URL, settings.SUPABASE_API_KEY
    )
    app.state.jwks_client = PyJWKClient(settings.SUPABASE_JWS_URL)
    app.state.transcriber = Transcriber(api_key=settings.ASSEMBLYAI_API_KEY)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(signin_router, prefix="")
```

Sets up, on startup: a Supabase admin client (stored on `app.state.supabase_admin`, consumed
by the auth feature's application layer), a `PyJWKClient` for verifying Supabase-issued JWTs,
and an AssemblyAI `Transcriber`. Mounts `signin_router` (see §1.1 for the transcript-router
duplication caveat).

---

## 5. Tests (`app/tests/`)

**`test_transcript.py`** — exercises `POST /transcript/` with a mocked `transcriber`
(`upload_file`/`transcribe` monkeypatched), asserting a 200 response with a `transcript` key.
Currently out of sync with `transcript.py`, where both the route and the `transcriber`
instance it patches are commented out.
