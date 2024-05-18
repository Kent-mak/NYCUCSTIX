
from DBClient import DBClient

DB_URI = "mongodb+srv://developer:cs15@cstix1.qizcotr.mongodb.net/?retryWrites=true&w=majority&appName=CSTIX1"
DB_NAME = 'Dev'
# Create a new client and connect to the server
db_client = DBClient(DB_URI, DB_NAME)



def sample_query():
    events = db_client.find(collection_name='Events') #events is a list of objects
    print(events)


if __name__ == '__main__':
    # Send a ping to confirm a successful connection
    try:
        db_client.ping()
        print(f"Pinged. Successfully connected to {DB_NAME}")
    except Exception as e:
        print(e)

    sample_query()
