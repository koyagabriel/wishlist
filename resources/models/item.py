from app import db

class Item(db.EmbeddedDocument):
    name = db.StringField(unique=True, required=True)
    link = db.StringField(required=True)
    price = db.FloatField(required=True)
    purchased = db.BooleanField(default=False)


    @property
    def get_name(self):
        return self.name

    @property
    def get_link(self):
        return self.link

    @property
    def get_price(self):
        return self.price

    @property
    def is_purchased(self):
        return self.purchased
