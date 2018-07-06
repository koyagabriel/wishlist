import factory
from resources.models.user import User


class UserFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = User

    username = factory.Faker('word', ext_word_list=None)
    password_hash = None
