from api.views.auth import Auth
from . import BaseItemTestCase

class CreateItemTestCase(BaseItemTestCase):
  
    def create_item_with_valid_params(self):

        # Act
        response = self.make('POST', '/items', payload=self.params, token=self.token)
        json_response = response.json
        data = json_response['data']

        # Assert
        self.assertTrue(response.status_code == 200)
        self.assertTrue(json_response['message'] == "Item Created")
        self.assertEqual(data['name'], 'hoodie')
