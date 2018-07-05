from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .item import Item

class User(db.Document):
    username = db.StringField(unique=True, required=True)
    password_hash = db.StringField(required=True)
    items = db.EmbeddedDocumentListField(Item)

    @property
    def get_username(self):
        return self.username

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
