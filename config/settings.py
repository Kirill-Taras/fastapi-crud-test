import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_name: str = "FastAPI CRUD Test"
    app_version: str = "1.0.0"
    database_url: str = os.getenv("DATABASE_URL", "")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "fastapi_db")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres1")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))


settings = Settings()
