from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schema import list_serial, individual_serial
from database import collection_name
from bson import ObjectId

router = APIRouter()

# get request method
# Home page
@router.get("/events/{event_name}", response_class=JSONResponse)
async def get_events(event_name: str):
    event = collection_name.find_one({"name": event_name})
    if event:
        return individual_serial(event)
        # return event
    else:
        return {"message": "Event not found"}
    # events = list_serial(collection_name.find())
    # return events
    

# @router.get("/")
# async def get():
#     events = list_serial(collection_name.find())
#     return events

# @router.post("/events/{}")
# async def choose_event(name: str = Form()):
#     return {"choose event = ": name}