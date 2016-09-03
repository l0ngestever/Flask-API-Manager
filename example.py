"""
    This is an example file who's uses Flask API Manager.
"""

from os import path
from random import getrandbits
from hashlib import sha256
from datetime import datetime

from flask_api_manager import Auth

from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


# Create some global vars
app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)


class ApiModel(db.Model):
    __tablename__ = "api"

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    secret = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    auth_get = db.Column(db.BOOLEAN)
    auth_post = db.Column(db.BOOLEAN)
    auth_put = db.Column(db.BOOLEAN)
    auth_delete = db.Column(db.BOOLEAN)
    date_created = db.Column(db.TIMESTAMP)
    date_deleted = db.Column(db.TIMESTAMP)
    last_connected = db.Column(db.TIMESTAMP)

    def __init__(self, name):
        self.name = name
        self.date_created = datetime.now()

        self.generate_secret()

    def __repr__(self):
        return "<API(id='%d', name='%s', secret='%s')>" % (self.id, self.name, self.secret)

    def generate_secret(self):
        self.secret = sha256(str(getrandbits(256)).encode('utf-8')).hexdigest()

    def connected(self):
        self.last_connected = datetime.now()

    def has_access(self, method):
        try:
            return getattr(self, "auth_%s" % method)
        except AttributeError:
            return False


# Time to create the auth model
auth = Auth(ApiModel)


class HelloWorld(Resource):
    @auth.auth('get')
    def get(self):
        return jsonify({'Message': 'Hello World!'})

    @auth.auth('post')
    def post(self):
        return jsonify({'Message': 'Hello World!'})

    @auth.auth('put')
    def put(self):
        return jsonify({'Message': 'Hello World!'})

    @auth.auth('delete')
    def delete(self):
        return jsonify({'Message': 'Hello World!'})


# Add some Configs to app.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(path.abspath(path.dirname(__file__)), 'app.db')


if __name__ in '__main__':
    # Before start first add some resources
    api.add_resource(HelloWorld, '/')

    # Time to FIRE
    app.run(debug=True, threaded=True)
