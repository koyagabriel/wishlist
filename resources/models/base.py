from app import db

class BaseDocument(db.Document):
    meta = {'abstract': True}

    @property
    def get_id(self):
        return str(self.id)
