from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # AssemblyAI
    ASSEMBLYAI_API_KEY: str = Field(default="", description="AssemblyAI API Key")

    # Qwen models
    ALIBABA_API_KEY: str = Field(default="", description="Alibaba API Key")
    ALIBABA_OPENAI_COMPATIBLE_ENDPOINT: str = Field(default="", description="Alibaba OpenAI Compatible Endpoint")
    ALIBABA_DASHCOPE: str = Field(default="", description="Alibaba DASHSCOPE Endpoint")
    
    # OpenRouter
    OPENROUTER_API_KEY: str = Field(default="", description="OpenRouter API Key")
    
    # OSS
    ALIBABA_OSS_BUCKET: str = Field(default="", description="Alibaba OSS Bucket Name")
    ALIBABA_OSS_ENDPOINT: str = Field(default="", description="Alibaba OSS Endpoint")
    ALIBABA_OSS_INTERNAL_ENDPOINT: str = Field(default="", description="Alibaba OSS Internal Endpoint")

    # Supabase
    SUPABASE_API_KEY: str = Field(default="", description="Supabase API Key")
    SUPABASE_URL: str = Field(default="", description="Supabase URL")
    SUPABASE_JWS_URL: str = Field(default="", description="Supabase JWS URL")
    
    # Groq
    GROQ_API_KEY: str = Field(default="", description="Groq Api Key")
    GROQ_BASE_URL: str = Field(default="", description="Groq OpenAI compatible URL")
    
    # Logging
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")

    # Configuration for Pydantic settings
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()