import falcon
import json
from pymongo import MongoClient
from libs.users import getUsers
client = MongoClient()
db = client.test_database


class Resource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        try:

            activity = getUsers()
            present_data = {
                'dev': activity[0],
                'user': activity[1],
                'epoch': activity[2]
            }
            resp.body = json.dumps(present_data)
            print('resp body', resp.body)
            resp.status = falcon.HTTP_200  # This is the default status
        except Exception as e:
            raise e


api = falcon.API()
api.add_route('/', Resource())
