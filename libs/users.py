from pymongo import MongoClient
client = MongoClient()
db = client.test_database
users = db.test_collection


def getUsers():
    cursor = db.test_collection.find().sort({$natural: -1}).limit(1)
    # print(cursor)