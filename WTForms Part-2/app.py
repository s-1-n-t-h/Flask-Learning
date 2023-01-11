from flask import Flask, render_template, flash, request
from form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nerchuko'

@app.route('/')
def home():
    return "Welcome to WTForms Tutorial"

@app.route('/contact',methods=['POST','GET'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All Fields are required!!')
            return render_template('contact.html',form=form)

        else:
            return 'Form Posted Successfully!'
    else:
        return render_template('contact.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
