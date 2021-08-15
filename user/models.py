from flask import Flask, jsonify, request, session, redirect

class User:
    def signup(self):
        print(request.form)

        user={
            "_id":"",
            "name": "",
            "email": "",
            "password":"" 
        }
        return jsonify(user), 200