from app import db

class BaseDocument(db.Document):
    meta = {'abstract': True}

    @property
    def get_id(self):
        return str(self.id)

    @classmethod
    def create(cls, params):
        return cls(**params).save()

    @classmethod
    def find_by_id(cls, id_):
        return cls.objects(id=id_).first()
