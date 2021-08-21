from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid
from hello import collection

class User:
    def signup(self):
        print(request.form)

        # user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        collection.insert_one(user)

        return jsonify(user), 200