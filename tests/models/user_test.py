import unittest
from tests import BaseTestCase
from resources.models.user import User
from tests.factories.user import UserFactory

class UserModelTestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.user = UserFactory.build()
        self.user.password = 'testing'

    def test_password_setter(self):
        self.assertTrue(self.user.password_hash is not None)

    def test_password_is_hashed(self):
        self.assertFalse(self.user.password_hash is 'testing')

    def test_no_password_getter(self):
        with self.assertRaises(AttributeError):
            self.user.password
