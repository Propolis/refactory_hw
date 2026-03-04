from pydantic import BaseModel, Field, field_validator
from typing import Optional


class BaseUser(BaseModel):
    username: str = Field(min_length = 4, max_length=19)
    name: str
    email: str
    #email: EmailStr - Встроенная в pydantic валидация Email. Тогда не нужно писать свой метод
    about: Optional[str] = None
    age: int = Field(ge=18, le=99)

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        return value


class CreateUser(BaseUser):
    id: int
    password: str


class UpdateUser(BaseModel):
    about: str