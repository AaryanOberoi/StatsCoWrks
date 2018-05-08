import os
import pymongo
from pymongo import MongoClient
client = MongoClient()

db = client.test_database

os.system("/bin/bash queues.sh")
fname = "devices.txt"
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print(f"Number of Active Devices: {num_lines - 3}")
os.system("/bin/bash ")

fname = "users.txt"
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print(f"Number of Active Users: {num_lines - 5}")
