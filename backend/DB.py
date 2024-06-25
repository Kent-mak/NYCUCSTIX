from pymongo.mongo_client import MongoClient
from typing import Optional

class DBClient():
    def __init__ (self, db_uri, dbname):
       self.mongodb_client = MongoClient(db_uri)
       self.database = self.mongodb_client[dbname]  # db name is Dev

   ## A quick way to test if we can connect to Atlas instance
    def ping (self):
       self.mongodb_client.admin.command('ping')

    def get_database(self):
        return self.database
    
    def get_collection (self, collection_name):
       collection = self.database[collection_name]
       return collection

    def find (self, collection_name, filter = {}, limit=0):
       collection = self.database[collection_name]
       items = list(collection.find(filter=filter, limit=limit))
       return items
   
    def user_format(self, user) -> dict:
        # user_collection = self.get_collection("User")
        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "password": user["password"],
            "events": user["events"]
        }
    
    def close(self):
        self.mongodb_client.close()
        return


class DBClientWrapper():
    def __init__(self):
        self.db_client: Optional[DBClient] = None

    def connect(self, uri, db_name):
        self.db_client = DBClient(uri, db_name)

    def get_client(self):
        return self.db_client

    def close(self):
        if self.db_client:
            self.db_client.close()

