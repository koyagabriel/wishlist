import unittest
import json
from tests import BaseTestCase
from tests.factories.user import UserFactory

class LoginTestCase(BaseTestCase):
  
    def setUp(self):
        super().setUp()
        self.user = UserFactory.build(username='admin')
        self.user.password = 'testing'
        self.user.save() 


    def test_login_with_valid_credentials(self):
        # Arrange
        params = {
            "username": self.user.get_username,
            "password": 'testing',
        }

        # Act
        response = self.make_request('POST', '/login', payload=params)
        json_response = response.json

        # Assert
        self.assertTrue(response.status_code == 200)
        self.assertTrue(json_response['message'] == "login successful")
        self.assertIsNotNone(json_response['data']['token'])


    def test_login_with_invalid_username(self):
        # Arrange
        params = {
            "username": 'wrong_username',
            "password": 'testing',
        }

        # Act
        response = self.make_request('POST', '/login', payload=params)
        json_response = response.json

        # Assert
        self.assertTrue(response.status_code == 401)
        self.assertTrue(json_response['message'] == "Invalid Credentials")
        self.assertFalse(json_response['success'])
    

    def test_login_with_invalid_password(self):
        # Arrange
        params = {
            "username": self.user.get_username,
            "password": 'wrong password',
        }

        # Act
        response = self.make_request('POST', '/login', payload=params)
        json_response = response.json

        # Assert
        self.assertTrue(response.status_code == 401)
        self.assertTrue(json_response['message'] == "Invalid Credentials")
        self.assertFalse(json_response['success'])
    

    
