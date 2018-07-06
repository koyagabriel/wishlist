from . import BaseItemTestCase
from tests.factories.item import ItemFactory

class GetItemTestCase(BaseItemTestCase):

    def get_item_with_id(self):
        # Arrange
        self.item = ItemFactory.create()

        # Act
        response = self.make('GET', f'/items/{self.item.get_id}', token=self.token)
        json_response = response.json
        data = json_response['data']

        # Assert
        self.assertTrue(response.status_code == 200)
        self.assertEqual(data['name'], self.item.get_name)
