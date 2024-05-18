def individual_serial(Events) -> dict:
    return{
        "id": str(Events["_id"]),
        "name": Events["name"],
        "Date": Events["Date"],
        "tickets_remaning": Events["tickets_remaning"]
    }
    
def list_serial(Events) -> list:
    return [individual_serial(Event) for Event in Events]