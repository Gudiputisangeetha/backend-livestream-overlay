from pymongo import MongoClient
from bson.objectid import ObjectId
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def get_collection(name):
    return db[name]

def serialize_doc(doc):
    if not doc:
        return None
    doc["_id"] = str(doc["_id"])
    return doc
