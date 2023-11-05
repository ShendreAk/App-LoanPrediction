import flask
import numpy as np
from flask import render_template, request, redirect
from utils import Model, Preprocess

app = flask.Flask(__name__)
app.config["debug"] = True

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/home/Predict", methods=["POST"])
def approved():
    if request.method =="POST":
        Total_amount = float(request.form['Amount'])
        Term = float(request.form['term'])
        Int_rate = np.round(float(request.form['int_rate']), 2)
        Installment = float(request.form['installment'])
        Annual_Income = float(request.form['annual_inc'])
        Dti = float(request.form['dti'])
        Open_account = float(request.form['open_acc'])
        Pub_rec = float(request.form['pub_rec'])
        Revol_balance = float(request.form['revol_bal'])
        Revol_util = float(request.form['revol_util'])
        Total_account = float(request.form['total_acc'])
        Mort_acc = float(request.form['mort_acc'])
        Bankruptcies = float(request.form['pub_rec_bankruptcies'])
        Grade = request.form['Subgrade']
        Verification_status = request.form['verification_status']
        Application_type = request.form['application_type']
        Initial_list_status = request.form['initial_list_status']
        Purpose = request.form['purpose']
        Home_ownership = request.form['home_ownership']
        Zipcode = int(request.form['zipcode'])
        Earliest_cr_year = int(request.form['earliest_cr_year'])

        features_list = [Total_amount,  Term, Int_rate, Installment, Annual_Income, Dti, Open_account, Pub_rec, Revol_balance, 
                         Revol_util, Total_account, Mort_acc, Bankruptcies, Grade, Verification_status, 
                         Application_type, Initial_list_status, Purpose, Home_ownership, Zipcode, Earliest_cr_year]
        processed = Preprocess(features_list)
        X_array = processed.out_array
        model = Model(X_array)
        pred = model.predict()
        pred = np.where(pred >0.5, 1,0)
        if pred == 1:
            return render_template("approved.html")
        else:
            return render_template("denied.html")
        return "Error"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)