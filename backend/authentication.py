from jose import jwt
from passlib.context import CryptContext
from dotenv import dotenv_values

config = dotenv_values(".env")
JWT_SECRTE_KEY = config["JWT_SECRTE_KEY"]
JWT_ALGORITHM = config["JWT_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# no need, except we store hash in database
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    encode_jwt = jwt.encode(to_encode, JWT_SECRTE_KEY, algorithm=JWT_ALGORITHM)
    return encode_jwt