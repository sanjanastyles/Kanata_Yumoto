from functools import wraps
from flask import Flask,g,render_template,request,abort, redirect, session, url_for
from flask.wrappers import Request 
from pymongo import MongoClient
from werkzeug import wrappers


app = Flask(__name__)
app.secret_key = 'SomeSecretKeyThatOnlyIShouldKnow'

# Database
cluster = MongoClient("mongodb+srv://sharplikekatana:12345@realmcluster.n5awq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

# Routes
from user import routes

def before_request(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/home')
    return wrap


@app.route('/home',methods=['GET', 'POST'])
def home():    
    if request.method == "POST":
        return redirect(url_for('welcome'))
    return render_template('home.html')

@app.route('/about',methods=['GET', 'POST'])
def about():
    if request.method == "POST":
        return redirect(url_for('welcome'))
    return render_template('about.html')


@app.route('/register',methods=['GET', 'POST'])
def register():
    return render_template('signup.html')


# @app.route('/login',methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         session.pop('user_id', None)

#         username = request.form['username']
#         password = request.form['password']
        
#         user = [x for x in users if x.username == username][0]
#          if user and user.password == password:
#              session['user_id'] = user.id
#              return redirect(url_for('profile'))

#         return redirect(url_for('login'))

#     return render_template('login.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    return render_template('login.html')

@app.route('/welcome',methods=['GET','POST'])
@before_request
def welcome():
    return render_template('welcome.html')

if __name__=='__main__':
    app.run(debug=True)
