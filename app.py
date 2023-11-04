import flask
import numpy as np
from flask import render_template, request, redirect
from utils import Predict

app = flask.Flask(__name__)
app.config["debug"] = True

@app.route("/")
def welcome():
    return render_template("approved.html")
@app.route("/home")
def home():
    return "Bye"

# @app.route("/Predict", methods=['GET',"POST"])
# def predict():
#     if request.method == 'POST':
#         return render_template("home.html")

# @app.route("/Predict/Approved", methods=["GET","POST"])
# def approved():
#     if request.method =="POST":
#         pred = []
#         if pred == 1:
#             return render_template("approved.html")
#         else:
#             return render_template("denied.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)