from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE_CONNECTION")

client = MongoClient(DATABASE, tlsAllowInvalidCertificates=True)

db = client['FAQ_Webapp']
collection_name = "library"
collection = db[collection_name]
def library_database_collection():
    return db['library']
def image_database_collection():
    return db['images']
# def school_database_collection():
        # return db['school']