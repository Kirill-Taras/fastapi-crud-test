import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_name: str = "FastAPI CRUD Test"
    app_version: str = "1.0.0"
    database_url: str = os.getenv("DATABASE_URL", "")


settings = Settings()
