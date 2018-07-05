from app import db

class BaseDocument(db.Document):
    meta = {'abstract': True}
