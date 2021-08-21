from flask import Flask,g,render_template,request,abort, redirect, url_for,session
from flask.wrappers import Request 
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = 'SomeSecretKeyThatOnlyIShouldKnow'

# Database
cluster = MongoClient("mongodb+srv://sharplikekatana:12345@realmcluster.n5awq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

# @app.before_request
# def before_request():
#     g.user = None

    # if 'user_id' in session:
    #     user = [x for x in users if x.id == session['user_id']][0]
    #     g.user = user

@app.route('/home',methods=['GET', 'POST'])
def home():    
    if request.method == "POST":
        name = request.form['name']
        return redirect(url_for('welcome', name=name))
    return render_template('home.html')

@app.route('/about',methods=['GET', 'POST'])
def about():
    if request.method == "POST":
        name = request.form['name']
        return redirect(url_for('welcome', name=name))
    return render_template('about.html')

# Routes
from user import routes
@app.route('/',methods=['GET', 'POST'])
def register():
    return render_template('signup.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    # if request.method == "POST":
    #     session.pop('user_id', None)

    #     username = request.form['username']
    #     password = request.form['password']
        
    #     user = [x for x in users if x.username == username][0]
    #      if user and user.password == password:
    #          session['user_id'] = user.id
    #          return redirect(url_for('profile'))

    #     return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

@app.route('/welcome/<name>',methods=['GET','POST'])
def welcome(name):
    return render_template('welcome.html',name=name)

if __name__=='__main__':
    app.run(debug=True)
