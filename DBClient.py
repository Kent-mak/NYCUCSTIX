from pymongo.mongo_client import MongoClient


class DBClient ():

    def __init__ (self, db_uri, dbname):
       self.mongodb_client = MongoClient(db_uri)
       self.database = self.mongodb_client[dbname]

    ## A quick way to test if we can connect to Atlas instance
    def ping (self):
        self.mongodb_client.admin.command('ping')

    def get_collection (self, collection_name):
        collection = self.database[collection_name]
        return collection

    def find (self, collection_name, filter = {}, limit=0):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit))
        return items
    
    def close(self):
        self.mongodb_client.close()
        return


