# flash alerts -- displays messages

from flask import Flask, url_for, render_template, request, redirect, session
from flask import flash

app = Flask(__name__)
app.secret_key = 'nerchuko'

@app.route('/')
def home():
    return f'Hello'

@app.route('/logout')
def logout():
    session.pop('user',None)
    flash('You have been logged out!','info')
    return redirect(url_for('login'))

@app.route('/login',methods=['POST',"GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['user']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        return render_template('login.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"You'r logged in as {user}"
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


