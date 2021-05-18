from pydantic import BaseModel
from typing import Optional

class LoginUser(BaseModel):
    username: str
    password: str


class CreateUser(BaseModel):
    username: str
    password: str
    email: str
    firstname: str
    lastname: str
