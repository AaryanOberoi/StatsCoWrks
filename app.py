import falcon
from pymongo import MongoClient
from libs.users import getUsers
from libs.upload import uploadCount
client = MongoClient()
db = client.test_database


class Resource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        try:
            active_users = getUsers()
            return
        except Exception as e:
            raise e

    def on_post(self, req, resp):
        try:
            # CRON GOES HERE
            uploadCount()
        except Exception as e:
            raise e


api = falcon.API()
api.add_route('/', Resource())
