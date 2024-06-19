from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from dotenv import dotenv_values
from DB import DBClient

config = dotenv_values(".env")
JWT_SECRTE_KEY = config["JWT_SECRTE_KEY"]
JWT_ALGORITHM = config["JWT_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = 300
DB_URI = config["ATLAS_URL"]
DB_NAME = config["DB_NAME"]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db_client = DBClient(DB_URI, DB_NAME)
database = db_client.get_database()
# no need, except we store hash in database
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)


# functions
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, JWT_SECRTE_KEY, algorithm=JWT_ALGORITHM)
    return encode_jwt 

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
                                status_code = status.HTTP_401_UNAUTHORIZED, 
                                detail = "Could not validate credentials",
                                headers = {"WWW-Authenticate": "Bearer"}
                            )
    try:
        payload = jwt.decode(token, JWT_SECRTE_KEY, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    
    return username
    # user = database.get_collection("Users").find_one({"name": username})
    # if user is None:
    #     raise credential_exception
    # return user

# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
    
#     return current_user