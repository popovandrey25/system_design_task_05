from pydantic import BaseModel, Field


class UserCreateRequest(BaseModel):
    """
    Схема для создания пользователя.
    """

    login: str = Field(..., examples=["johndoe"])
    password: str = Field(..., examples=["secret"])
    first_name: str = Field(..., examples=["John"])
    last_name: str = Field(..., examples=["Doe"])


class UserResponse(BaseModel):
    """
    Схема для ответа.
    """
    id: int
    login: str
    full_name: str

    class Config:
        from_attributes = True


class TokenRequest(BaseModel):
    """
    Схема для запроса токена (логин/пароль).
    """

    username: str
    password: str


class TokenResponse(BaseModel):
    """
    Схема для ответа при успешной аутентификации.
    """

    access_token: str
    token_type: str = "bearer"
