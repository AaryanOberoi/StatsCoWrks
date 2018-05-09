from pymongo import MongoClient
# import pprint
# import pymongo
client = MongoClient()
db = client.test_database
collection = db.test_collection

# Timestamp is a datetime object in UTC time

# pprint.pprint(
# 	posts.find_one({"date": epoch difference less than 5 minutes => -2211753300}))


# def UTC_time_to_epoch(timestamp):
#     epoch = calendar.timegm(timestamp.utctimetuple())
#     return epoch

cur = db.test_collection.find()
a = list(cur)
b = sorted(a, key=lambda k: k['epoch'], reverse=1)
print('Device Count :')
print({b[0]['devicecount']}, {b[0]['date']})
print('User Count : ')
print({b[0]['usercount']}, {b[0]['date']})
# print(sorted(list(cur), 'epoch')

# cur.sort('test_collection.epoch', -1).limit(1)
# for doc in cur:
# print(doc)
