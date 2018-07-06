from flask import request, g
from resources.models.item import Item as ItemModel
from api.decorators import verify_access, catch_exceptions
from api.utils import respond_to_json

class Item:

    @classmethod
    @verify_access
    @catch_exceptions
    def post(cls):
        params = request.json
        params.update({"user_id": g.id})
        item = ItemModel.create(params)
        return respond_to_json(message='Item Created', data={"item": item})

    @classmethod
    @verify_access
    @catch_exceptions
    def get(cls, id):
        item = ItemModel.find_by_id(id)
        if not item:
            return respond_to_json(message='Item was not found', status=404, success=False)
        return respond_to_json(message='Item was found', data={"item": item})

    @classmethod
    @verify_access
    @catch_exceptions
    def update(cls, id):
        params = request.json
        item = ItemModel.find_by_id(id)
        if not item:
            return respond_to_json(message='Item does not exist', status=400, success=False)
        item.update(**params)
        return respond_to_json(message='Item was updated', data={"item": item.reload()})

    @classmethod
    @verify_access
    @catch_exceptions
    def delete(cls, id):
        item = ItemModel.find_by_id(id)
        if not item:
            return respond_to_json(message='Item does not exist', status=400, success=False)
        item.delete()
        return respond_to_json(message='Item has been deleted')
