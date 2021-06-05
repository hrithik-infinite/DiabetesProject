import pickle
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

mod1 = pickle.load(open('logistic_mod2.pkl','rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route("/predict", methods = ['POST'])
def diab():
    age_ip = float(request.form['age'])
    glucose_ip = float(request.form['glucose'])
    bp_ip = float(request.form['bp'])
    skin_ip = float(request.form['skin'])
    insulin_ip = float(request.form['insulin'])
    preg_ip = float(request.form['preg'])
    bmi_ip = float(request.form['bmi'])
    pedigree_ip = float(request.form['pedigree'])

    lis = [preg_ip,glucose_ip,bp_ip,skin_ip,insulin_ip,bmi_ip,pedigree_ip,age_ip]
    list = [lis]
    pred = mod1.predict(list)

    if(pred[0] == 0):
        answer = "You are not suffering from diabetes"
    else:
        answer = "You are suffering from diabetes"


    return render_template('index.html', ans = answer)


if __name__ == '__main__':
    app.run(debug = True)
