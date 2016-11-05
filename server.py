from flask import Flask, url_for, render_template, redirect, request, session, escape
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
    try:
        return render_template('homepage.html',user=session['user'])
    except:
        return render_template('Login.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('Login.html')
    print 'this' # MOST IMPORTANT LINE AT HACKHOLYOKE
                 # DON'T REMOVE!!!!!!!!!!!
    user = request.form['loginUsername']
    print request.form
    if db_pass_query(user, request.form['loginPassword']):
        print 'Logged in\n'
        session['user'] = user
        print session
        return redirect(url_for('index'))
    
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = request.form['username'] #Get user/pass for user ID
    psk  = request.form['password']
    db.posts.insert_one({'user':user,'pass':psk}) # Append user to logindb
    session['user'] = user
    redirect('http://goo')
    return 

@app.route('/test',methods=['GET','POST'])
def test():
    try:
        return render_template('test.html',user=session['user'])
    except:
        return render_template('test.html',user='FAILED')

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host='0.0.0.0',port=80)
