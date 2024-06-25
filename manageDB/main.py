from fastapi import FastAPI, Request
from DBClient import DBClient
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from bson import json_util
import datetime

DB_URI = "mongodb://167.99.69.49:27017/"
DB_NAME = 'CSTIX'
# Create a new client and connect to the server
db_client = DBClient(DB_URI, DB_NAME)
app = FastAPI()

def eventExist(event_name):
    events = db_client.find(collection_name='Events') #events is a list of objects
    
    for event in events:
        if event["name"] == event_name:
            return True
    return False

def userExist(user_name):
    users = db_client.find(collection_name='Users') #events is a list of objects
    for user in users:
        if user["name"] == user_name:
            return False
    return True


@app.post("/insert_event")
async def insert_event(request: Request):
    # name, photo, description, tickets_remaining, year, month, day, hour, minute, price, location
    Events = db_client.database['Events'] 
    entry = await request.form()
    if eventExist(entry['name']):
        print("event already exist")
        return JSONResponse(content="event already exist", status_code=409)

    result = Events.insert_one(entry)
    print(f'Data inserted with IDs: {result.inserted_ids}')
    
    return JSONResponse(
        content= f'Data inserted with IDs: {result.inserted_ids}',
        status_code=200
    )

@app.put('/reset_users')
async def resetUsers():

    reset_users = {"$set": {"events": []}}
    result = db_client.database['Users'].update_many({}, reset_users)
    print(result.upserted_id)
    return JSONResponse(
        content="User reset success",
        status_code=200
    )


@app.put('/edit_user')
async def editUser(request: Request):
    json_data= await request.json()
    user_name = json_data['user_name']
    update = json_data['update']
    try:
        result = db_client.database["Users"].update_one({"name": user_name},{"$set":update})
        print(f"modified {result.modified_count} documents.")
    except Exception as e:
        print(f"Error: {e}")


@app.put('/edit_event')
async def editUser(request: Request):
    json_data = await request.json()
    event_name = json_data['event_name']
    update = json_data['update']
    try:
        result = db_client.database["Events"].update_one({"name": user_name},{"$set":update})
        print(f"modified {result.modified_count} documents.")
    except Exception as e:
        print(f"Error: {e}")
