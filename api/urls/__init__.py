from api import api
from api.views import index

api.add_url_rule('/',  endpoint='homepage', view_func=index, methods=['GET'],
                 strict_slashes=False)
