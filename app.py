from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

# Load the model 
model = pickle.load(open('model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

# Creating the Flask app 
app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict(): 
    # Extracting the data 
    age = int(request.form['age'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    charges = int(request.form['charges'])
    sex = request.form['sex']
    smoker = request.form['smoker']
    region = request.form['region']

    # One-hot encoding for sex, smoker and children
    sex_1 = sex 

    smoker_1 = smoker

    region_1 = 1 if region == 1 else 0 
    region_2 = 1 if region == 2 else 0 
    region_3 = 1 if region == 3 else 0 

    children_1 = 1 if children == 1 else 0
    children_2 = 1 if children == 2 else 0
    children_3 = 1 if children == 3 else 0
    children_4 = 1 if children == 4 else 0
    children_5 = 1 if children == 5 else 0

if __name__ == "__main__":
    app.run(debug=True)
