from pydantic import  BaseModel
from typing import  Optional

class User(BaseModel):
    id: str
    username:str
    email: Optional[str]= None
    fristname: Optional[str] = None
    lastname: Optional[str] = None
    password:str
