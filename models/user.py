from pydantic import BaseModel, Field
from settings import settings


class User(BaseModel):
    """
    Пользователь интернет-магазина.
    """
    id: int = Field(title="Код пользователя")
    user_family: str = Field(title="Фамилия", max_length=settings.USER_NAME_LEN)
    user_name: str = Field(title="Имя", max_length=settings.USER_NAME_LEN)
    user_email: str = Field(title="E-Mail", max_length=settings.EMAIL_LEN)
    user_password: str = Field(
        title="Пароль",
        max_length=settings.PASSWORD_MAX_LEN,
        min_length=settings.PASSWORD_MIN_LEN,
    )


class UserIn(BaseModel):
    """
    Пользователь интернет-магазина - добавление.
    """
    user_family: str = Field(title="Фамилия", max_length=settings.USER_NAME_LEN)
    user_name: str = Field(title="Имя", max_length=settings.USER_NAME_LEN)
    user_email: str = Field(title="E-Mail", max_length=settings.EMAIL_LEN)
    user_password: str = Field(
        title="Пароль",
        max_length=settings.PASSWORD_MAX_LEN,
        min_length=settings.PASSWORD_MIN_LEN,
    )