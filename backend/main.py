from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI, Form, Request, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from model import Events, User
import os
from DB import DBClientWrapper
from dotenv import dotenv_values
from contextlib import asynccontextmanager
from schema import list_serial_events, individual_serial_events, list_serial_user, individual_serial_user, individual_serial_problems, list_serial_problems
from authentication import create_access_token, get_current_user
import uuid
from bson import Binary
from Problem import generate_p_token, get_random_problem
import random
from SolveTask import solve_task
from datetime import datetime, timezone

config = dotenv_values(".env")
DB_URI = config["MONGO_URL"]
DB_NAME = config["DB_NAME"]

db_client_wrapper = DBClientWrapper()
database = None
# define lifespan method for fastapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_db_client(app)
    yield
    await shutdown_db_client(app)

async def startup_db_client(app):
    global database
    db_client_wrapper.connect(DB_URI, DB_NAME)
    database = db_client_wrapper.get_client().get_database()
    try:
        db_client_wrapper.get_client().ping()
        print("DB connected!")
    except Exception as e:
        print(f"Failed to connect to DB, raise error: {e}")
        
async def shutdown_db_client(app):
    db_client_wrapper.get_client().close()
    print("Database disconnected.")

# create server with python FastAPI
app = FastAPI(lifespan=lifespan)

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


def eventExist(event_name):
    events =  database.get_collection("Events").find()
    for event in events:
        if event["name"] == event_name:
            return True
    return False

# endpoints:
# # homepage
@app.get("/")
async def read_form(request: Request):
    events = list(database.get_collection("Events").find())
    for event in events:
        event['_id'] = str(event['_id'])
    return events

# # handle login
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
    print(event_name)
    # event = collection_name.find_one({"name": event_name})
    event = database.get_collection("Events").find_one({"name": event_name})
    if event:
        return individual_serial_events(event)
        # return event
    else:
        return {"message": "Event not found"}

# handle register


# handle login
@app.post("/token")
# async def login(accountName: str = Form(...), password: str = Form(...)):
async def login(form_data: OAuth2PasswordRequestForm = Depends()): 
    user = database.get_collection("Users").find_one({"name": form_data.username})
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if form_data.password != user["password"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token = create_access_token(data={"sub": user["name"]})
    
    response = JSONResponse({
        "code": 0,
        "msg": "successfully login!",
        "user_name": user["name"],
        "access_token": access_token,
        "token_type": "bearer"
    })

    return response
    # return {"username": username, "password": password}


# only login user can access this endpoint
@app.get("/user_data")
async def user_page(token):
    user_name = await get_current_user(token)
    print(user_name)
    user = database.get_collection("Users").find_one({"name": user_name})
    user['_id'] = str(user['_id'])
    print(user)
    return user

@app.post("/checkans")
async def verify_answer(request: Request):
    # check if this exist in DB
    body = await request.json()
    access_token = body["access_token"]
    p_token = body["p_token"]
    ans = body["ans"]
    print(p_token)
    print("recieved:")
    print(repr(ans))

    
    print(type(p_token))
    p_token = uuid.UUID(p_token)
    p_token = Binary.from_uuid(p_token)
    print(type(p_token))
    answer = database.get_collection("Problems").find_one({"p_token": p_token})
    # collection = database.get_collection("Problems").find()
    # return list_serial_problems(collection)
    print("correct:")
    print(repr(answer["ans"]))
    if answer == None:  # if the token is not exist
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="You are using an invalid token."
        )
    if ans[-1] != '\n' and answer["ans"][-1] == '\n':
        ans += '\n'
    print(repr(ans))
    if answer["ans"] != ans:  # answer incorrect
        print("ans incorrect")
        database.get_collection("Problems").delete_one({"p_token": p_token})
        print("successfully deleted")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Your answer is wrong! You idiot."
        )
        
    else:  # the answer is correct
        # find user with access token
        print("access_token:", access_token)
        user_name = await get_current_user(access_token)
        print("user_name = ", user_name)
        # user = database.get_collection("Users").find_one({"name": user_name})
        update_user = database.get_collection("Users")\
                                    .update_one(
                                        {"name": user_name, "events.name": answer["event_name"]},  # event need to check what is in database
                                        {"$inc": {"events.$.count": 1}}
                                    )
        print(f"matched count {update_user.matched_count}")
        if update_user.matched_count == 0:
            add_ticket = database.get_collection("Users").update_one(
                {"name": user_name},
                {"$push": {"events": {"name": answer["event_name"], "count": 1}}}
            )


            # raise HTTPException(
            #     status_code=status.HTTP_404_NOT_FOUND,
            #     detail="update user database failed."
            # )
        
        # delete p_token in problems
        database.get_collection("Problems").delete_one({"p_token": p_token})
        content = {"msg": "your answer is correct! brilliant!"}
        return JSONResponse(content=content, status_code=200)
    
    
@app.get('/get_problem')
async def get_problem(token, event_name):

    if not eventExist(event_name):
        raise HTTPException(
            status_code=404,
            detail="Event doesn't exist"
        )


    p_token, p_token_non_Binary = generate_p_token()
    p_id = get_random_problem(event_name)
    print(p_id)
    try:
        problem = database.get_collection("ProblemContents").find_one({"id": p_id})
    except Exception as e:
        print(f'Exception: {e}')

    var = random.randint(int(problem['var_start']), int(problem['var_end']))
    ans = solve_task(int(p_id), var)
    print(f'var: {var}')
    print(f'ans: {ans}')
    try:
        result = database.get_collection("Problems").insert_one({
            "p_token": p_token,
            "ans": str(ans),
            "access_token": token,
            "event_name": event_name,
            "createdAt": datetime.now(timezone.utc)
        })

        print(f'inserted: {result.inserted_id}')

    except Exception as e:
        print(f'error occurred while getting problem: {e}')
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'error occurred while getting problem: {e}',
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    print(type(p_token_non_Binary))
    response = {
        "p_token": p_token_non_Binary,
        "p_id": p_id,
        "content": problem['content'],
        "var": var,
        "name": problem['name']
    }

    return response
