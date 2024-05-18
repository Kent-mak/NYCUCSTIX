from pydantic import BaseModel, BeforeValidator, Field
from bson import ObjectId
from typing import Annotated

# represent _id (type = ObjectId in database -> bson) as str (to encode as json)
PyObjectId = Annotated[str, BeforeValidator(str)]

class Events(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alies="_id")
    name: str
    Date: str
    tickets_remaning: int
    