from os import name
from flask import Flask, jsonify, session, redirect,request
from passlib.hash import pbkdf2_sha256
import uuid
from hello import collection

class User:
 
    def create_account(self,name,email,password):
        print(request.form)

        # user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": name,
            "email": email,
            "password": password
        }
        
        # encrypt password 
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        #already existing emails
        if collection.find_one({ "email": user['email'] }):
            return jsonify({ "error": "Email address already in use" }), 400

        if collection.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "signup failed"}), 400

    def start_session(self,user):
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user) , 200
        
    def signout(self):
        session.clear()
        return redirect('/home')

    def login(self):

        user = collection.find_one({
            "email" : request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        return jsonify({ "error" : "Invalid login credentials"}), 401