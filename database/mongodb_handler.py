from pymongo import MongoClient
from datetime import datetime

mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['smart_home']

def insert_into_mongodb(collection_name, data):
    data['timestamp'] = datetime.utcnow() 
    collection = mongo_db[collection_name]
    collection.insert_one(data)
