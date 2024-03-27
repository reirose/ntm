from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.get_database("news-to-mongo")
coll = db.get_collection("news")
