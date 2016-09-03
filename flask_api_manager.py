#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps
from flask import jsonify, request

from sqlalchemy import and_


__version__ = '0.1.0'


class Auth:
    """
        Auth class have some values:
          * model
            - This is the original SQAlchemy model, which have the API settings inside.
    """

    model = None

    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return "<Auth(model='%s')>" % self.model

    def check_auth(self, method):
        api_consumer = self.model.query.filter(and_(self.model.name == request.authorization.username,
                                                    self.model.secret == request.authorization.password)).first()
        if api_consumer:
            if api_consumer.has_access(method):
                return True
            return False
        return False

    def authenticate(self, message):
        message = {'Message': message}
        resp = jsonify(message)

        resp.status_code = 401
        resp.headers['WWW-Authenticate'] = 'Basic realm="API"'

        return resp

    def auth(self, method):
        def auth(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                if not request.authorization:
                    return self.authenticate("Not authenticated.")

                elif not self.check_auth(method):
                    return self.authenticate("Not authorized.")

                return f(*args, **kwargs)
            return decorated
        return auth
