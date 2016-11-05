from flask import Flask, render_template, redirect, request, session, escape
from pymongo import MongoClient
from flask.ext.login import LoginManager, UserMixin, login_required
import trader

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

