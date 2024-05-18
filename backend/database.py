from pymongo import MongoClient

client = MongoClient('mongodb+srv://developer:cs15@cstix1.qizcotr.mongodb.net/?retryWrites=true&w=majority&appName=CSTIX1')

db = client['Dev']

collection_name = db['Events']