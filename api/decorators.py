from functools import wraps
from flask import request, g
from .utils import respond_to_json


def catch_exceptions(f):
   
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            res = f(*args, **kwargs)
        except Exception:
            return respond_to_json(message='An error occurred', 
                                   status=500, success=False)
        return res
    return decorated_function

def verify_access(f):
    from api.views.auth import Auth
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.has_key('Authorization') or not request.headers['Authorization']:
            return respond_to_json(message='Access denied. Token was not sent', status=401, success=False)   
        token = request.headers['Authorization']
        try:
            payload = Auth.verify_token(token)
        except Exception:
            return respond_to_json(message='Invalid Token', status=401, success=False)  
        g.id = payload['id']
        return f(*args, **kwargs)
    return decorated_function