import unittest
import json
from flask import current_app
from base64 import b64encode
from app import create_app, db

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        config = self.app.config
        db.connection.drop_database(config['MONGODB_SETTINGS']['db'])
        self.app_context.pop()


    def get_api_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def make_request(self, method, path, payload=None):
        data = json.dumps(payload)
        client = self.client
        kwargs = {'data': data, 'headers': self.get_api_headers()}
        return {
            'POST': client.post,
            'GET': client.get,
            'PUT': client.put,
            'DELETE': client.delete
        }[method](path, **kwargs)
