from flask import Flask, render_template, redirect, request, session, escape
from pymongo import MongoClient
from flask.ext.login import LoginManager, UserMixin, login_required
import trader

login_manager = LoginManager()
mdbClient = MongoClient()
db = mdbClient.Login_DB
app = Flask(__name__)
login_manager.init_app(app)

# Users: Kyle [kztoth], jon [none]
def db_pass_query(user,password):
    posts = db.posts
    try:
        psk = posts.find_one({'user':user})['pass']
        return psk == password
    except:
        return False    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    user = request.form['username']
    if db_pass_query(user, request.form['password']):
        print 'Logged in\n'
        session['user'] = user
        print session
    return render_template('index.html')
    
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = request.form['username'] #Get user/pass for user ID
    psk  = request.form['password']
    db.posts.insert_one({'user':user,'pass':psk}) # Append user to logindb
    session['user'] = user
    return render_template('test.html',user=session['user'])

@app.route('/test')
def test():
    try:
        return render_template('test.html',user=session['user'])
    except:
        return render_template('test.html',user='FAILED')

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host='0.0.0.0',port=80)
