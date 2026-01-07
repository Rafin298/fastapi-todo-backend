from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    # DATABASE_URL: str = "sqlite:///./todos.db"
    DATABASE_URL: str = "postgresql://postgres:1234@localhost:5432/todos_db"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
