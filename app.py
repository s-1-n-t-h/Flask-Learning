from flask import Flask, redirect, url_for

app = Flask(__name__) #creating instance of flask

@app.route('/') # directs to default home page denoted by /
def home():
    return "<h1>Let's Learn Flask!</h1>"

@app.route('/courses') # directs to a specific web page named after /
def courses():
    return "Welcome to My Website!"

@app.route('/<name>') # dynamic routing
def name(name):
    return f'Hello {name}'

@app.route('/admin') # redirection to home page when clicked for actually another web page
def admin():
    #return redirect('/') # redirect methods from flask library
    return redirect(url_for('courses')) # can also be done using function name of a particular route

if __name__ == '__main__':
    app.run(debug=True)





