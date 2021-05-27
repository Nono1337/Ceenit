from pydantic import BaseModel

class CreateList(BaseModel):
    name: str
    description: str = ""


