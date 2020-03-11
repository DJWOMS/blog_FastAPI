from pydantic.main import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    user_id: int = None


class Msg(BaseModel):
    msg: str
