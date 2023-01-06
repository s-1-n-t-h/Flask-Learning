from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        # url_for() function is used to build a URL to the specific function dynamically
        return redirect(url_for('user', usr=user))
    return render_template('login.html')

    # The first argument is the name of the specified function, and then we can pass any number of keyword argument corresponding to the variable part of the URL.

@app.route('/<usr>')
def user(usr):
    return f"Hello {usr}"
if __name__ == "__main__":
    app.run(debug=True)