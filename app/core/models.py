from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Models(BaseSettings):
    # AssemblyAI
    ASSEMBLYAI_MODELS:list[str] = Field(
        default=["universal-2", "universal-3-pro", "universal-3-5-pro"],
        description="AssemblyAI models in fallback order"
    )
    
    # Qwen
    ALIBABA_MODELS:list[str] = Field(
        default=["qwen3.7-flash", "qwen3.5-flash"],
        description="Qwen models in fallback order"
    )


models = Models()