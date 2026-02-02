## 🚀 Bank Customer Classification Using AdaBoost

This project implements a **supervised machine learning pipeline** to predict whether a bank customer will subscribe to a product, using **AdaBoost with Decision Trees** as the classifier.

---

## 📂 Dataset Overview

- **Training Data**: `bank_customers_train.csv`
- **Test Data**: `bank_customers_test.csv`
- **Target Column**: `y` (`yes` / `no`)
- **Features**: Numerical and categorical attributes related to customer demographics, job, and banking activity

The task is a **binary classification** problem.

---

## 🧩 Project Workflow

---

## 1️⃣ Data Loading & Cleaning
- Load datasets using **Pandas**
- Handle missing values:
  - Drop rows with missing critical features (`job`, `marital`)
  - Fill missing categorical features with the **mode**
- Map categorical columns to numeric representations

---

## 2️⃣ Feature Encoding & Scaling
- **Label Encoding** for categorical variables (`job`, `marital`)
- **Mapping** for ordinal features (`education`, `month`, `day_of_week`, `poutcome`)
- **Min-Max Scaling** for numeric columns (`pdays`, `emp.var.rate`, `cons.price.idx`, etc.)
- Convert binary features to 0/1 format

---

## 3️⃣ Train–Test Split
- Split the training data into:
  - **80% training**
  - **20% validation**
- Ensures model evaluation on unseen data

---

## 4️⃣ Model Training (AdaBoost)
- Algorithm: **AdaBoost Classifier**
- Base estimator: **Decision Tree** (max depth=4, min samples split=5)
- Key hyperparameters:
  - `n_estimators = 100`
  - `learning_rate = 0.1`

The model is trained on preprocessed training data.

---

## 5️⃣ Model Evaluation
- Generate predictions on validation set
- Evaluate performance using:
  - **F1-score** for positive class (`yes`)
- Example F1-score: `0.566`

---

## 6️⃣ Test Data Prediction
- Apply the trained model to unseen test data
- Convert predictions to 0/1 format
- Output structured as a **DataFrame** for submission

---

## 🛠️ Tools & Technologies

- **Programming Language**: Python
- **Data Handling**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (AdaBoostClassifier, DecisionTreeClassifier)
- **Preprocessing**: LabelEncoder, MinMaxScaler, Mapping, Train-Test Split

---

## 🎯 Conclusion

This project demonstrates a complete **binary classification workflow**, including:
- Data cleaning and imputation
- Categorical encoding
- Feature scaling
- AdaBoost model training and evaluation
- Prediction on unseen data

It highlights the effectiveness of **ensemble methods** for tabular data with mixed numerical and categorical features.

