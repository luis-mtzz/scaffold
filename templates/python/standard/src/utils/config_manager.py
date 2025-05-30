# src/utils/config_manager.py
from pydantic import BaseSettings, PostgresDsn, Field

class Settings(BaseSettings):
    app_name: str = "Sample App"
    environment: str = "development"
    debug: bool = False

    # Database
    database_url: PostgresDsn = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()