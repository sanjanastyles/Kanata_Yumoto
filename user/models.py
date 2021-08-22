from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid
from hello import collection

class User:
    def signup(self, name, email, password):

        # user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": name,
            "email": email,
            "password": password
        }

        # encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        collection.insert_one(user)

        return jsonify(user), 200