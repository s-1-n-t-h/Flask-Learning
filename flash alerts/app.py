from flask import Flask, url_for, render_template, reuquest, session
from datetime import timedelta
from flask import flash

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        