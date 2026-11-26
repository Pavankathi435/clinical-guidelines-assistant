from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql://postgres:postgres@localhost:5432/clinical"
    redis_url: str = "redis://localhost:6379/0"
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    cohere_api_key: str = ""
    embedding_model: str = "BAAI/bge-small-en-v1.5"  # 384 dims
    cache_threshold: float = 0.92
    cache_ttl_seconds: int = 86400


settings = Settings()