import uuid
import random
import bson.binary
from dotenv import dotenv_values
from bson.binary import Binary


config = dotenv_values(".env")


def generate_p_token():
    uuid_token = uuid.uuid4()
    return Binary.from_uuid(uuid_token, uuid_representation=4), uuid_token

def get_random_problem(event_name: str):
    if event_name == "新手村":
        return 6
    return random.randint(1, int(config["PROBLEM_COUNT"])-1)