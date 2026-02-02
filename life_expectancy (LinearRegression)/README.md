## 🏥 Life Expectancy Prediction Using Polynomial Regression

This project implements a **supervised machine learning regression pipeline** to predict **life expectancy** using country-level health, economic, and demographic features.  
The objective is to train a model on historical data, evaluate its performance, and generate predictions for unseen countries.

---

## 📂 Dataset Overview

- **Training Data**: `train.csv`
- **Test Data**: `test.csv`
- **Target Column**: `Life expectancy`
- **Features**: Various numerical and categorical indicators (e.g., Population, GDP, Health Expenditure, Vaccination Rates, BMI, Alcohol Consumption, Schooling)

The dataset is structured for a **regression task**.

---

## 🧩 Project Workflow

The project follows a standard regression pipeline:

---

## 1️⃣ Data Loading
- Load training and test datasets using **Pandas**
- Separate features and target labels from the training data

---

## 2️⃣ Data Preprocessing
- Handle missing values:
  - Fill numerical features using **group-wise mean** per country
  - Fill remaining missing values with **median**
- Drop irrelevant columns (e.g., `Country`, `Status` where appropriate)

---

## 3️⃣ Feature Scaling & Transformation
- Apply **StandardScaler** to normalize features
- Generate **polynomial features (degree=2)** to capture non-linear relationships

Why polynomial features?  
> Non-linear relationships often exist between health indicators and life expectancy, improving model accuracy.

---

## 4️⃣ Model Training
- Algorithm: **Linear Regression** on polynomial features
- Fit the model on the scaled and transformed training data

---

## 5️⃣ Model Evaluation
- Evaluate model performance using:
  - **R² score**  
- Achieved **R² ≈ 0.875** on training data

---

## 6️⃣ Test Data Prediction
- Apply preprocessing and polynomial transformation to test data
- Generate predictions
- Store predictions in a structured **DataFrame**
- Ready for submission or further analysis

---

## 🛠️ Tools & Technologies

- **Programming Language**: Python
- **Data Handling**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (LinearRegression, PolynomialFeatures, StandardScaler)

---

## 🎯 Conclusion

This project demonstrates a complete **regression workflow**, including:
- Data preprocessing
- Feature scaling
- Polynomial feature generation
- Model training and evaluation
- Prediction on unseen data

It emphasizes the importance of preprocessing and feature engineering to capture non-linear relationships in real-world datasets.

