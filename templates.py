from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # diaplys home.html file stored in templates folder
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html') # diaplys index.html file stored in templates folder 


if __name__ == '__main__':
    app.run(debug=True)

