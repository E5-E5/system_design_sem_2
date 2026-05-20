from pydantic import BaseModel

class Hotel(BaseModel):
    id: str
    name: str
    city: str
    address: str
    description: str