from tests import BaseTestCase

class BaseItemTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.user = UserFactory.build(username='admin')
        self.user.password = 'testing'
        self.user.save()
        self.token = Auth.generate_token({
            "username": self.user.get_username,
            "id": self.user.get_id
        })
        self.params = {
            "name": "hoodie",
            "link": "http://wwww.google.com",
            "price": 23.0
        }
