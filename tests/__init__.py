import unittest
import json
from flask import current_app
from app import create_app, db

class BaseTestCase(unittest.TestCase):
    _headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        config = self.app.config
        db.connection.drop_database(config['MONGODB_SETTINGS']['db'])
        self.app_context.pop()
