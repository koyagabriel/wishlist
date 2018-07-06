from api import api
from api.views.item import Item


api.add_url_rule('/items', endpoint='Item_post', methods=['POST'], view_func=Item.post,
                 strict_slashes=False)
api.add_url_rule('/items/<id>', endpoint='Item_get', methods=['GET'], view_func=Item.get,
                 strict_slashes=False)
api.add_url_rule('/items/<id>', endpoint='Item_update', methods=['PUT'], view_func=Item.update,
                 strict_slashes=False)
api.add_url_rule('/items/<id>', endpoint='Item_delete', methods=['DELETE'], view_func=Item.delete,
                 strict_slashes=False)
