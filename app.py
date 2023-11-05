import flask
import numpy as np
from flask import render_template, request, redirect
from utils import Predict

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
        Zipcode = request.form['zipcode']
        earliest_cr_year = int(request.form['earliest_cr_year'])
        pred = []
        if pred == 1:
            return render_template("approved.html")
        else:
            return render_template("denied.html")
        return "BYE"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)