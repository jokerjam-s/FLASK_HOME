from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    USER_NAME_LEN: int
    EMAIL_LEN: int
    PRODUCT_NAME_LEN: int
    PASSWORD_MIN_LEN: int
    PASSWORD_MAX_LEN: int

    class Config:
        env_file = ".env"


settings = Settings()
