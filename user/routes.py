from flask import Flask, jsonify, request, session, redirect
from hello import app
from user.models import User

@app.route('/user/signup',methods=['GET','POST'])
def signup():
    
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    return User().signup(name,email,password)