from pydantic import BaseModel


class User(BaseModel):
    id: int
    login: str
    password: str
    first_name: str
    last_name: str