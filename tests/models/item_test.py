import unittest
from tests import BaseTestCase
from resources.models.item import Item
from tests.factories.item import ItemFactory

class UserModelTestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.item = ItemFactory.build(
            name = 'Shoe',
            link = 'http://www.shoe.com',
            price = 2.00
        )

    def test_name_property_getter(self):
        self.assertTrue(self.item.get_name == 'Shoe')

    def test_link_property_getter(self):
        self.assertTrue(self.item.get_link == 'http://www.shoe.com')

    def test_price_property_getter(self):
        self.assertTrue(self.item.get_price == 2.00)

    def test_purchased_defaults_to_false(self):
        self.assertFalse(self.item.is_purchased)
