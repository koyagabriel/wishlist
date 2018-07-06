from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .item import Item
from .base import BaseDocument

class User(BaseDocument):
    username = db.StringField(unique=True, required=True)
    password_hash = db.StringField(required=True)

    @property
    def get_username(self):
        return self.username

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @classmethod
    def find_by_username(cls, username):
        return cls.objects(username=username).first()

    @classmethod
    def post(cls, params):
        return cls(
            username=params["username"],
            password_hash=generate_password_hash(params['password'])
        ).save()
