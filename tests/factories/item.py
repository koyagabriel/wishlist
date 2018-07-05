import factory
from resources.models.item import Item


class ItemFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Item

    name = factory.Faker('word', ext_word_list=None)
    link = factory.Faker('word', ext_word_list=None)
    price = factory.Faker('pyfloat', positive=True)
    purchased = False
