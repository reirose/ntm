from pymongo import MongoClient
from os import getenv

client = MongoClient(f"mongodb://mongodb:27017")
# client = MongoClient(f"{getenv('mongodb://mongodb:27017')}")
db = client.get_database("news-to-mongo")
coll = db.get_collection("news")
