
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from DBClient import DB_Client
from dotenv import dotenv_values
from contextlib import asynccontextmanager
from routes import router
from schema import list_serial
from database import collection_name
config = dotenv_values(".env")
DB_URL = config["ATLAS_URL"]
DB_NAME = config["DB_NAME"]

# defind lifespan mwthod for fatsapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_db_client(app)
    yield
    await shutdown_db_client(app)

async def startup_db_client(app):
    app.db_client = DB_Client(DB_URL, DB_NAME)
    try:
        app.db_client.ping()
        print("MongoDB connected!")
    except Exception as e:
        print(f"Failed to connect to MongoDB, raise error: {e}")
        
async def shutdown_db_client(app):
    app.db_client.close()
    print("Database disconnected.")
    
# not used     
# def sample_query():
#     events = db_client.find(collection_name='Events') #events is a list of objects
#     print(events)

# create server with python FastAPI
app = FastAPI(lifespan=lifespan)
app.include_router(router)

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/template")

# homepage
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    events = list(collection_name.find())
    return templates.TemplateResponse("page.html", {"request": request, "events": events})

# after submit form -> redirect to corresponding page
@app.post("/submit-form")
async def handle_form(event_name: str = Form(...)):
    redirect_url = f"/events/{event_name}"
    return RedirectResponse(url=redirect_url, status_code=303)
