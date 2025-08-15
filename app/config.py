# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App meta
    APP_NAME: str = Field(default="MHN Portfolio API")

    # Env vars (set these on Render)
    DATABASE_URL: str = Field(default="sqlite:///./app.db")
    ALLOWED_ORIGINS: str = Field(
        default="http://localhost:8000, https://nirob-0812.github.io"
    )
    ADMIN_TOKEN: str = Field(default="dev-admin-token")
    SECRET_KEY: str = Field(default="change-me")

    @property
    def sqlalchemy_url(self) -> str:
        """
        Convert Postgres URL to psycopg3 SQLAlchemy URL when needed.
        e.g. postgresql://...  -> postgresql+psycopg://...
             postgres://...    -> postgresql+psycopg://...
        """
        url = self.DATABASE_URL
        if url.startswith("postgres://"):
            return url.replace("postgres://", "postgresql+psycopg://", 1)
        if url.startswith("postgresql://") and "+psycopg" not in url:
            return url.replace("postgresql://", "postgresql+psycopg://", 1)
        return url

    @property
    def cors_origins(self) -> list[str]:
        return [o.strip() for o in self.ALLOWED_ORIGINS.split(",") if o.strip()]


settings = Settings()


# Backwards-compatible helper (used by main.py)
def get_cors_origins() -> list[str]:
    return settings.cors_origins
