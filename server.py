from flask import Flask, url_for, render_template, redirect, request, session, escape, json
from pymongo import MongoClient
# from flask.ext.login import LoginManager, UserMixin, login_required
from trader import Merchandise, Trader, getUserByField

#login_manager = LoginManager()
mdbClient = MongoClient()
db = mdbClient.Login_DB
app = Flask(__name__)
#login_manager.init_app(app)

# Users: Kyle [kztoth], jon [none]
def db_pass_query(user,password):
    posts = db.posts
    try:
        psk = posts.find_one({'user':user})['pass']
        return psk == password
    except:
        return False    

@app.route('/results')
def results():
    return render_template('result.html',user=session['user'])

@app.route('/')
def index():
#    try:
    loop = {'jon':'peach','kyle':'car','keith':'computer'}
    itemList = ['peach','car','computer']
    return render_template('homepage.html',user=session['user'],i=itemList)
#    except:
#        print session['user']
#        print "Failed"
#        return render_template('Login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('Login.html')
    user = request.form['loginUsername']
    if db_pass_query(user, request.form['loginPassword']):
        print 'logged in'
        session['user'] = user
        return redirect(url_for('index'))
    
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = request.form['username'] #Get user/pass for user ID
    psk  = request.form['password']
    db.posts.insert_one({'user':user,'pass':psk}) # Append user to logindb
    session['user'] = user
    redirect(url_for('index'))
    return 

@app.route('/addItemGive',methods=['GET','POST'])
def addItem():
    item = str(request.form['item'])
    trader1 = getUserByField('username',str(session['user']))
    item = Merchandise({'name':item})
    trader1.createMerch(item)
    return 'OK'

@app.route('/addItemGet',methods=['GET','POST'])
def addItemGet():
    item = str(request.form['item'])
    trader1 = getUserByField('username',str(session['user']))
    item = Merchandise({'name':item})
    trader1.addWantedMerch(item)
    return 'OK'

@app.route('/delete1',methods=['GET','POST'])
def delete1():
    r = request.form['value']
    r = r.replace(' ','').strip('\n')
    trader1 = getUserByField('username',str(session['user']))
    item = [i.details['name'] for i in trader1.enumerateWantedMerch()]
    ite = [i for i in trader1.enumerateWantedMerch()]
    i = item.index(str(r))
    remove = ite[i]
    trader1.destroyMerch(remove)
    return 'OK'

@app.route('/delete',methods=['GET','POST'])
def delete():
    r = request.form['value']
    r = r.replace(' ','').strip('\n')
    trader1 = getUserByField('username',str(session['user']))
    item = [i.details['name'] for i in trader1.enumerateMerch()]
    ite = [i for i in trader1.enumerateMerch()]
    i = item.index(str(r))
    remove = ite[i]
    trader1.destroyMerch(remove)
    return 'OK'

@app.route('/add',methods=['GET','POST'])
def add():
    trader1 = getUserByField('username',str(session['user']))
    requestList = [i.details['name'] for i in trader1.enumerateWantedMerch()]
    tradingList = [x.details['name'] for x in trader1.enumerateMerch()]
    return render_template('add.html',user=session['user'],tradingList=tradingList,requestList=requestList)



if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host='0.0.0.0',port=80)
