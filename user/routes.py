from flask import Flask
from hello import app
from user.models import User

@app.route('/user/signup',methods=['GET','POST'])
def signup():
  return User().signup()
