from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def prdict():
    weight = request.form['weight']
    height = request.form['height']

    weight,height = float(weight),float(height)

    height = height/100

    bmi = weight/(height**2)

    bmi = round(bmi,2) 

    if bmi > 0:
        if bmi<=16:
            return render_template('result.html', pred=f'Your BMI is:{bmi}. You are Sevierly Under Weight')
        elif bmi <= 18.5:
            return render_template('result.html', pred=f'Your BMI is:{bmi}. You are Under Weight')
        elif bmi <= 25:
            return render_template('result.html', pred=f'Your BMI is:{bmi}. You are Healthy')
        elif bmi <= 30:
            return render_template('result.html', pred=f'Your BMI is:{bmi}. You are Over Weight')
        else:
            return render_template('result.html', pred=f'Your BMI is:{bmi}. You are Severely Over Weight')
    else:
        return render_template('result.html',pred='Enter Correct Details of weight and height')

if __name__ == '__main__':
    app.run(debug=True)