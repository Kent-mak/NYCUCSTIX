from fastapi import FastAPI
from DBClient import DBClient
from bson import json_util
import json

DB_URI = "mongodb+srv://developer:cs15@cstix1.qizcotr.mongodb.net/?retryWrites=true&w=majority&appName=CSTIX1"
DB_NAME = 'Dev'
# Create a new client and connect to the server
db = DBClient(DB_URI, DB_NAME)
app = FastAPI()


@app.get("/")
async def root():
    events = db.find(collection_name='Events')
    print(events)

    return json.loads(json_util.dumps(events))