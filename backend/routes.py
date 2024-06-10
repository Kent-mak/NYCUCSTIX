from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schema import list_serial, individual_serial
from DBClient import DBClient
from bson import ObjectId
from dotenv import dotenv_values

router = APIRouter()
config = dotenv_values(".env")
DB_URI = config["ATLAS_URL"]
DB_NAME = config["DB_NAME"]
db_client = DBClient(DB_URI, DB_NAME)
database = db_client.get_database()

# get request method
# event page
@router.get("/events/{event_name}", response_class=JSONResponse)
async def get_events(event_name: str):
    event = database.get_collection("Events").find_one({"name": event_name})
    if event:
        return individual_serial(event)
        # return event
    else:
        return {"message": "Event not found"}
    # events = list_serial(collection_name.find())
    # return events
