from typing import List
from bson import Binary

def individual_serial_events(event) -> dict:
    return{
        # "id": str(event["_id"]),
        "name": event["name"],
        "photo": event['photo'],
        "description": event["description"],
        # "date": event["date"],
        # "tickets_remaning": event["tickets_remaining"],
        # "price": event['price'],
        # "location": event['location'],
        "vote_count": event['vote_count']
    }


def list_serial_events(events) -> list:
    return [individual_serial_events(event) for event in events]
    
    
def individual_serial_tickets(ticket) -> dict:
    return {
        "count": int(ticket["count"]),
        "eventID": str(ticket["eventID"])
    }

def list_serial_tickets(tickets) -> dict:
    return [individual_serial_tickets(ticket) for ticket in tickets]

def individual_serial_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        # "password": user['password'],
        "events": user['events']
    }

def list_serial_user(users) -> list:
    return [individual_serial_user(user) for user in users]


def individual_serial_problems(problem) -> dict:
    return{
        "ans": str(problem["ans"]),
        "access_token": str(problem["access_token"]),
        "event_name": str(problem["event_name"]),
        "p_token": Binary.as_uuid(problem["p_token"])
    }
    
def list_serial_problems(problems) -> list:
    return [individual_serial_problems(problem) for problem in problems]
