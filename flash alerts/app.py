from flask import Flask, url_for, render_template, request, session, redirect
from datetime import timedelta
from flask import flash

app = Flask(__name__)
app.secret_key = 'secret_key'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['name']
        session['user'] = user
        flash('login successful', 'success')
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash('You are already Logged In')
            return redirect(url_for('user'))
        return render_template('login.html')

 
@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template('user.html')
    else:
        flash('You are not logged in')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user',None)
    flash("You have been logged out!",'warning')
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)