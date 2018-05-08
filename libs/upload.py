import datetime
from pymongo import MongoClient
client = MongoClient()
db = client.test_database
collection = db.test_collection
fname = "devices.txt"
num_lines1 = 0
num_lines2 = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines1 += 1
queuecount = num_lines1 - 3
# print(f"Number of Active Devices: {queuecount}")
fname = "users.txt"
with open(fname, 'r') as f:
    for line in f:
        num_lines2 += 1
xchangcount = num_lines2 - 5
# print(f"Number of Active Users: {xchangcount}")
post = {
    "devicecount": queuecount,
    "usercount": xchangcount,
    "date": datetime.datetime.utcnow()}
db.test_collection.insert(post)
# Inserting the count into table
