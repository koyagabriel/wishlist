import unittest
import json
from tests import BaseTestCase

class RegistrationTestCase(BaseTestCase):


    def test_registration_with_valid_input(self):
        # Arrange
        params = {
            "username": "admin",
            "password": "pwd",
            "confirm_password": "pwd"
        }

        # Act
        response = self.make_request('POST', '/register', payload=params)
        json_response = response.json

        # Assert
        self.assertTrue(response.status_code == 200)
        self.assertTrue(json_response['message'] == "Successfully Registered")
    

    def test_registration_with_password_mismatch(self):
        # Arrange
        params = {
            "username": 'test',
            "password": 'pass',
            "confirm_password": 'element'
        }

        # Act
        response = self.make_request('POST', '/register', payload=params)
        json_response = response.json

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertTrue(json_response['message'] == "Password mismatch")
        self.assertFalse(json_response['success'])

