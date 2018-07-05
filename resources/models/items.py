from app import db

class Item(db.Document):
    name = db.StringField(unique=True, required=True)
    link = db.StringField(required=True)
    price = db.IntField(required=True)
    purchased = db.BooleanField(default=False)


    @classmethod
    def create(cls, params):
        return cls.objects(**params).save()


    @classmethod
    def get(cls, id):
        item = cls.objects(id=id).first()

        if not item: raise ValueError(f'{cls.__name__} with an id of {id} does not exist')

        return item

    @classmethod
    def update(cls, id, params):
        item = cls.get(id)

        return item.updat(**params)

    @classmethod
    def delete(cls, id):
        item = cls.get(id)

        return item.delete()
