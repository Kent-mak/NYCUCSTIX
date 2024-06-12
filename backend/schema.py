def individual_serial_events(event) -> dict:
    return{
        "id": str(event["_id"]),
        "name": event["name"],
        "Date": event["Date"],
        "tickets_remaning": event["tickets_remaning"]
    }

def individual_serial_user(user) -> dict:
    return{
        "id": str(user["_id"]),
        "name": str(user["name"])        
    }

def list_serial_events(events) -> list:
    return [individual_serial_events(event) for event in events]

def list_serial_user(users) -> list:
    return [individual_serial_user(user) for user in users]