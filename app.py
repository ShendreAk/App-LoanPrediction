import flask
import numpy as np
from flask import render_template, request, redirect
from utils import Predict

app = flask.Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/Predict", methods=['GET',"POST"])
def predict():
    if request.method == 'POST':
        return render_template("home.html")

@app.route("/Predict/Approved", methods=["GET","POST"])
def approved():
    if request.method =="POST":
        pred = []
        if pred == 1:
            return render_template("approved.html")
        else:
            return render_template("notapproved.html")