from flask import current_app
from . import BaseTestCase
from app import create_app, db

class SetupTestCase(BaseTestCase):

    def test_app_exist(self):
        """tests whether a false return is gotten for a non existing app"""
        self.assertFalse(current_app is None)

    def test_app_has_testing_config(self):
        """
        tests the configuration setup if it returns true if an application is
        created
        """
        self.assertTrue(current_app.config["TESTING"])
