from pydantic import BaseModel, BeforeValidator, Field
from bson import ObjectId
from typing import Annotated, List

# represent _id (type = ObjectId in database -> bson) as str (to encode as json)
PyObjectId = Annotated[str, BeforeValidator(str)]

class Events(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    Date: str
    tickets_remaning: int
    
class Tickets(BaseModel):
    count: int
    eventID: str


class User(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str | None = None
    password: str
    events: List[Tickets] = []
