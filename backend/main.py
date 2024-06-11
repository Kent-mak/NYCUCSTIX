
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI, Form, Request, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from model import Events, LoginForm
import os
from DBClient import DBClient
from dotenv import dotenv_values
from contextlib import asynccontextmanager
# from routes import router
from schema import list_serial_events, individual_serial_events, list_serial_user, individual_serial_user
from authentication import verify_password, get_password_hash, create_access_token

config = dotenv_values(".env")
DB_URI = config["ATLAS_URL"]
DB_NAME = config["DB_NAME"]

# defind lifespan mwthod for fatsapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_db_client(app)
    yield
    await shutdown_db_client(app)

async def startup_db_client(app):
    app.db_client = DBClient(DB_URI, DB_NAME)
    try:
        app.db_client.ping()
        print("MongoDB connected!")
    except Exception as e:
        print(f"Failed to connect to MongoDB, raise error: {e}")
        
async def shutdown_db_client(app):
    app.db_client.close()
    print("Database disconnected.")

# create server with python FastAPI
app = FastAPI(lifespan=lifespan)
db_client = DBClient(DB_URI, DB_NAME)
database = db_client.get_database()
# app.include_router(router)

# app.mount("/frontend", StaticFiles(directory="static"), name="static")
template_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'frontend', 'template')
templates = Jinja2Templates(directory=template_path)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# endpoints:
# # homepage
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    events = list(database.get_collection("Events").find())
    return templates.TemplateResponse("page.html", {"request": request, "events": events})

# handle login
# @app.get("/", response_class=HTMLResponse)
# async def read_form(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})



# after submitform -> redirect to corresponding new page
@app.post("/submit-form")
async def handle_form(event_name: str = Form(...)):
    redirect_url = f"/events/{event_name}"
    return RedirectResponse(url=redirect_url, status_code=303)\
      
      
# handle 
@app.get("/events/{event_name}", response_class=JSONResponse)
async def get_events(event_name: str):
    # event = collection_name.find_one({"name": event_name})
    event = database.get_collection("Events").find_one({"name": event_name})
    if event:
        return individual_serial_events(event)
        # return event
    else:
        return {"message": "Event not found"}

# handle register


# handle login
@app.post("/login/")
async def login(accountName: str = Form(...), password: str = Form(...)):
    user = database.get_collection("Users").find_one({"name": accountName})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.name}
    )
    response = JSONResponse({
        "code": 0,
        "msg": "successfully login!"
    })
    
    # user = users.find_one({"name": user})
    return response
    # return {"username": username, "password": password}
