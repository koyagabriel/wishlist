from flask import request, jsonify, current_app
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from werkzeug.security import generate_password_hash, check_password_hash
from resources.models.user import User
from api.utils import respond_to_json

class Auth:

    @staticmethod
    def generate_token(payload):
        serializer = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
        return serializer.dumps(payload).decode(encoding='ascii')


    @staticmethod
    def _verify_token(token):
        serializer = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = serializer.loads(token)
        except BadSignature or SignatureExpired:
            return None


    @staticmethod
    def _verify_password(password, user):
        return check_password_hash(user.password_hash, password)


    @classmethod
    def register(cls):
        params = request.json
        if params['password'] != params['confirm_password']:
            return respond_to_json(success=False,
                                   message="Password mismatch",
                                   status=400)

        if User.find_by_username(params['username']):
            return respond_to_json(success=False,
                                   message="Username has already been taken",
                                   status=400)

        user = User.post(params)

        if user:
            token = cls.generate_token({"username": user.username,
                                         "id": user.get_id})

        return respond_to_json(message="Successfully Registered",
                              data={"username": user.username, "token": token})


    @classmethod
    def login(cls):
        username, password = request.json['username'], request.json['password']
        user = User.find_by_username(username)
        if not user:
            return respond_to_json(success=False,
                                   message="Invalid Credentials",
                                   status=401)

        if not cls._verify_password(password, user):
            return respond_to_json(success=False,
                                   message="Invalid Credentials",
                                   status=401)

        token = cls.generate_token({"username": user.username, "id": user.get_id})

        return respond_to_json(message='login successful',
                               data={"username": user.username, "token": token})
