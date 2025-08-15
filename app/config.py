from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "Mehedi Hasan Nirob — Portfolio"
    DATABASE_URL: str = "sqlite:///./app.db"
    ALLOWED_ORIGINS: str = "*"
    ADMIN_TOKEN: str = "changeme"

    class Config:
        env_file = ".env"

settings = Settings()

def get_cors_origins() -> List[str]:
    raw = settings.ALLOWED_ORIGINS or "*"
    return [o.strip() for o in raw.split(",") if o.strip()]
