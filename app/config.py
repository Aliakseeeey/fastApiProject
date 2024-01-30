from pydantic_settings import BaseSettings
from pydantic import root_validator


class Settings(BaseSettings):
    BD_USER: str
    BD_PORT: int
    BD_HOST: str
    BD_PASS: str
    BD_NAME: str

    @root_validator(skip_on_failure=True)
    def get_database_url(cls, v):
        v["DATABASE_URL"] = f"postgresql+asyncpg://{v['BD_USER']}:{v['BD_PASS']}@{v['BD_HOST']}:{v['BD_PORT']}/{v['BD_NAME']}"
        return v

    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()

