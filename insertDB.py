
from DBClient import DBClient 
from bson.objectid import ObjectId
from datetime import datetime

# DB_URI = "mongodb+srv://developer:cs15@cstix1.qizcotr.mongodb.net/?retryWrites=true&w=majority&appName=CSTIX1"
DB_URI = "mongodb://root:donthackcscamp2024@167.99.69.49:27017/"
DB_NAME = 'CSTIX'
# Create a new client and connect to the server
db_client = DBClient(DB_URI, DB_NAME)

def eventExist(event_name):
    events = db_client.find(collection_name='Events') #events is a list of objects
    
    for event in events:
        if event["name"] == event_name:
            return False
    return True

def userExist(user_name):
    users = db_client.find(collection_name='Users') #events is a list of objects
    for user in users:
        if user["name"] == user_name:
            return False
    return True


def insertEvents():
    Events = db_client.database['Events'] 
    data = []
    while True:
        
        name = input("name: ")
        if not eventExist(name):
            print("event already exist")
            continue
        photo = input("photo url: ")
        description = input("description: ")
        tickets_remaining = input("tickets remaining: ")
        year = int(input("year: "))
        month = int(input("month: "))
        day = int(input("day: "))
        hour = int(input("hour: "))
        minute = int(input('minute: '))
        price =int(input("price: "))
        location = input("location: ")

        entry = {
            "name": name,
            "photo": photo,
            "description": description,
            "tickets_remaining": tickets_remaining,
            "date": datetime(year, month, day, hour, minute),
            "price": price,
            "location": location
        }
        if input("add to list?: "):
            data.append(entry)

        if(int(input("insert more?: ")) != 1):
            break

    print(f'entries to be added: {data}')
    if input("commit?: "): 
        result = Events.insert_many(data)
        print(f'Data inserted with IDs: {result.inserted_ids}')
    else:
        print("Input cancelled")


def insertUsers():
    Users = db_client.database['Users'] 
    data = []
    while True:
        
        name = input("name: ")
        if not userExist(name):
            print("user already exist")
            continue
        photo = input("photo url: ")
        password = input("password: ")

        entry = {
            "name": name,
            "photo": photo,
            "password": password,
            "events": []
        }

        if input("add to list?: "):
            data.append(entry)

        if(int(input("insert more?: ")) != 1):
            break

    print(f'entries to be added: {data}')
    if input("commit?: "): 
        result = Users.insert_many(data)
        print(f'Data inserted with IDs: {result.inserted_ids}')
    else:
        print("Input cancelled")
    

if __name__ == "__main__":
    try:
        db_client.ping()
        print(f"Pinged. Successfully connected to {DB_NAME}")
      
        if int(input('insert Events?: ')):
            insertEvents()

        if int(input('insert Users?: ')):
            insertUsers()
    
    except Exception as e:
        print(e)

    
