from pymongo import MongoClient
from os import getenv

# client = MongoClient(f"{getenv('MONGO_URI')}")
client = MongoClient(f"{getenv('mongodb://localhost:27017')}")
db = client.get_database("news-to-mongo")
coll = db.get_collection("news")
