from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "供应链知识库"
    debug: bool = False

    # CORS
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    # Database
    database_url: str = "sqlite:///./knowledge_base.db"
    redis_url: str = "redis://localhost:6379/0"

    # Vector store
    chroma_persist_dir: str = "./chroma_data"
    embedding_model: str = "text-embedding-3-small"

    # LLM
    default_llm_provider: str = "claude"
    anthropic_api_key: str = ""
    anthropic_base_url: str = ""  # override for compatible providers (e.g. MiniMax)
    anthropic_model: str = "claude-sonnet-4-20250514"  # override via ANTHROPIC_MODEL
    openai_api_key: str = ""
    deepseek_api_key: str = ""

    # RAG
    chunk_size: int = 512
    chunk_overlap: int = 50
    top_k: int = 5

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
