# Insurance Claim Prediction Web App

This Flask-based web application predicts whether a person is likely to make an insurance claim based on user input. It uses a machine learning model (Random Forest or Logistic Regression) trained on scaled and preprocessed data.

## 🚀 Project Structure

```
insurance-claim-app/
├── app.py
├── model.pkl
├── scaler.pkl
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

## 🧠 ML Details

- Models used: Logistic Regression & Random Forest
- Data preprocessing:
  - Outlier handling
  - One-Hot Encoding (categorical features)
  - StandardScaler (numerical features)
  - SMOTE (to address imbalance)

## 📦 Setup Instructions

1. **Clone this repo**
   ```bash
   git clone <repo-url>
   cd insurance-claim-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**
   ```bash
   python app.py
   ```

4. **Open the browser**
   Go to `http://127.0.0.1:5000`

## ✍️ Input Features (in this order)

1. age
2. bmi
3. charges
4. sex_male
5. smoker_yes
6. children_1
7. children_2
8. children_3
9. children_4
10. region_northwest
11. region_southeast
12. region_southwest

> Note: Categorical features are one-hot encoded. Only one child/region should be marked as 1.

## 📂 Files Explained

- `app.py`: Flask app for model deployment
- `model.pkl`: Trained machine learning model
- `scaler.pkl`: Trained StandardScaler for numerical features
- `templates/index.html`: Web UI for user input and prediction
- `requirements.txt`: Python dependencies

## 🛠️ Requirements

```txt
Flask
scikit-learn
numpy
pandas
```

You can generate `requirements.txt` with:
```bash
pip freeze > requirements.txt
```

## 📌 Future Enhancements

- Add dropdowns/radios for better UI
- Display probability more visually
- Handle missing or invalid inputs gracefully

---

Made with ❤️ for Machine Learning Deployment!


