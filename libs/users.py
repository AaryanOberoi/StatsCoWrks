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

def getUsers():
    cur = db.test_collection.find()
    a = list(cur)
    b = sorted(a, key=lambda k: k['epoch'], reverse=1)
    dev = b[0]['devicecount']
    user = b[0]['usercount']
    epoch = b[0]['epoch']
    # print(f'Device Count : {dev}')
    # print(f'User Count : {user}')
    # print({b[0]['date'], b[0]['epoch']}) return b[0]
    data_count = [dev, user, epoch]
    return data_count
# print(sorted(list(cur), 'epoch')
# cur.sort('test_collection.epoch', -1).limit(1)
# for doc in cur:
# print(doc)


if __name__ == '__main__':
    getUsers()
