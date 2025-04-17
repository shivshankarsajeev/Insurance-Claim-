from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect input data from the form
        age = float(request.form["age"])
        bmi = float(request.form["bmi"])
        charges = float(request.form["charges"])
        sex = int(request.form["sex"])         # 1 for male, 0 for female
        smoker = int(request.form["smoker"])   # 1 for smoker, 0 for non-smoker
        region = int(request.form["region"])   # 1, 2, 3; if 0 then region_0 (dropped)
        children = int(request.form["children"])  # 0 to 5

        # One-hot encode the categorical variables
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

        # Scale the numerical features using a DataFrame to avoid warning
        scaled_features = scaler.transform(pd.DataFrame([[age, bmi, charges]], columns=['age', 'bmi', 'charges']))
        age_scaled, bmi_scaled, charges_scaled = scaled_features[0]

        # Create the final input array in the same order as training
        final_input = np.array([[
            age_scaled, bmi_scaled, charges_scaled,
            sex_1, children_1, children_2, children_3, children_4, children_5,
            smoker_1, region_1, region_2, region_3
        ]])

        prediction = model.predict(final_input)
        output = "Claimed" if prediction[0] == 1 else "Not Claimed"

        return render_template("index.html", prediction_text=f"Insurance can be {output}")

    except ValueError:
        return render_template("index.html", prediction_text="Please enter valid numerical values.")

if __name__ == "__main__":
    app.run(debug=True)