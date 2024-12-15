from typing import List, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    AUTH_TOKEN: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
