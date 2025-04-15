#  Insurance Claim Prediction Web App

This Flask-based web application allows users to **predict the likelihood of an insurance claim** being made, based on health and demographic inputs. It leverages machine learning models trained on preprocessed data to deliver real-time predictions through a simple web interface.

---

## 📝 Description

Insurance claim prediction is a critical task in the healthcare insurance industry, aiming to anticipate whether a policyholder will claim insurance. This helps companies in **risk assessment, fraud detection**, and **premium pricing**.

In this project, we built a **classification model** using a sample insurance dataset. While the dataset is relatively small and slightly imbalanced, it presents a challenging yet practical problem in predictive modeling.

The model classifies whether an insurance claim is likely (`1`) or not (`0`) based on various user inputs such as age, BMI, smoking habits, and region.

---

## 📊 Dataset Overview

The dataset contains the following features:

| Feature         | Description |
|-----------------|-------------|
| `age`           | Age of the policyholder |
| `sex`           | Gender (female = 0, male = 1) |
| `bmi`           | Body Mass Index – weight in relation to height |
| `steps`         | Average walking steps per day |
| `children`      | Number of children/dependents |
| `smoker`        | Smoking status (non-smoker = 0, smoker = 1) |
| `region`        | Residential area in the US (northeast=0, northwest=1, southeast=2, southwest=3) |
| `charges`       | Medical costs billed to health insurance |
| `insuranceclaim`| Target variable: Claim made (yes = 1, no = 0) |

> 📌 **Note**: This dataset is derived from the [Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance) on Kaggle.

---

## 🧠 Machine Learning Pipeline

- **Models Used**:
  - Logistic Regression
  - Random Forest Classifier

- **Data Preprocessing Includes**:
  - Handling outliers
  - One-Hot Encoding for categorical features (`sex`, `smoker`, `children`, `region`)
  - Scaling numerical values using `StandardScaler`
  - Addressing class imbalance with `SMOTE`

---

## 📂 Project Structure

```
insurance-claim-app/
├── app.py                  # Flask application
├── model.pkl               # Trained ML model
├── scaler.pkl              # Fitted StandardScaler
├── templates/
│   └── index.html          # Frontend for user input and prediction display
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 💻 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repo-url>
   cd insurance-claim-app
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App**
   ```bash
   python app.py
   ```

4. **Access the Web Interface**  
   Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## 🧾 Input Features (Order-Sensitive)

The app expects the following **scaled and one-hot encoded features** in this exact order:

1. `age`  
2. `bmi`  
3. `charges`  
4. `sex_male`  
5. `smoker_yes`  
6. `children_1`  
7. `children_2`  
8. `children_3`  
9. `children_4`  
10. `region_northwest`  
11. `region_southeast`  
12. `region_southwest`

> ⚠️ Note: Features are transformed using one-hot encoding and scaled prior to model input.

---

## 📦 Requirements

```
Flask  
scikit-learn  
numpy  
pandas
```

Generate `requirements.txt` using:
```bash
pip freeze > requirements.txt
```

---

## 🌟 Future Enhancements

- Replace text fields with dropdowns/radio buttons for better UX  
- Visualize prediction probability using charts or progress bars  
- Add input validation and error handling  
- Enable batch prediction via CSV upload

---

## 🎯 Objective

- Understand and clean the dataset  
- Perform data preprocessing and feature transformation  
- Train classification models to predict whether an insurance claim will be made  
- Tune hyperparameters and compare multiple algorithms (Logistic Regression, Random Forest, etc.)  
- Evaluate performance using accuracy, precision, recall, F1-score, and ROC-AUC

---

## 🙏 Acknowledgements

- Dataset Source: [Medical Cost Personal Datasets - Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance)