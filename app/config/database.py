from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_collection():
    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME")
    col_name = os.getenv("COLLECTION_NAME")

    client = MongoClient(uri)
    db = client[db_name]
    return db[col_name]