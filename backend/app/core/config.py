import os
from enum import Enum
from typing import List

from pydantic import BaseSettings
from pydantic.networks import AnyHttpUrl


class AppEnvironment(str, Enum):
    PRODUCTION = "production"
    DEV = "development"
    TESTING = "testing"


class Config(BaseSettings):
    """
    Base configuration.
    """

    API_V1_STR = "/api/v1"

    APP_VERSION: str = "Unversioned API"
    FASTAPI_ENV: AppEnvironment = AppEnvironment.DEV

    UVICORN_HOST: str = "0.0.0.0"
    UVICORN_PORT: int = 8000

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str | None = "FastAPI app template"

    SENTRY_ENABLED: bool | None = False
    SENTRY_DSN: str | None = ""
    SENTRY_ENV: str | None = "dev"

    DATABASE_URI: str = "sqlite:///./app.db"

    LOGGING_LEVEL: str = "INFO"

    def is_dev(self) -> bool:
        return self.FASTAPI_ENV == AppEnvironment.DEV

    def is_prod(self) -> bool:
        return self.FASTAPI_ENV == AppEnvironment.PRODUCTION


settings = Config(_env_file=".env", _env_file_encoding="utf-8")
