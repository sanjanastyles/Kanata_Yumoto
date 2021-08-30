from flask import Flask, request
from hello import app
from user.models import User


@app.route('/user/signup',methods=['GET','POST'])
def signup():
  name = request.form['name']
  email = request.form['email']
  password = request.form['password']
  return User().create_account(name,email,password)

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login',methods=['GET','POST'])
def login():
  return User().login()