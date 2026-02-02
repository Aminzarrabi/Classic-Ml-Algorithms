# 📚 Machine Learning & Data Analysis Projects

This repository contains **five ML & data analysis projects**, covering **classification, regression, and clustering** tasks.  
Each project has its own folder with scripts, preprocessing, and data files.

---

## 🗂 Projects Overview

### 1️⃣ Bank Customer Classification
- **Goal:** Predict if a customer subscribes to a term deposit.
- **Algorithm:** AdaBoost with DecisionTreeClassifier
- **Dataset:** `bank_customers_train.csv`, `bank_customers_test.csv`
- **Key Points:**
  - Handles missing categorical data
  - Label encoding and scaling applied
  - Model evaluated using **F1-score**

---

### 2️⃣ Life Expectancy Prediction
- **Goal:** Predict life expectancy for countries.
- **Algorithm:** Linear Regression with Polynomial Features
- **Dataset:** `train.csv`, `test.csv`
- **Key Points:**
  - Numerical feature imputation
  - Standard scaling
  - Polynomial feature engineering
  - Evaluated using **R² score**

---

### 3️⃣ Mall Customer Segmentation
- **Goal:** Segment customers based on demographic and spending data.
- **Algorithm:** K-Means Clustering
- **Dataset:** `mall_customers.csv`
- **Key Points:**
  - Preprocessing includes encoding gender and dropping IDs
  - Model finds **5 customer segments**
  - Silhouette score used to evaluate clustering quality
  - Visualizations: bar charts, histograms

---

### 4️⃣ Mushroom Classification
- **Goal:** Classify mushrooms as edible or poisonous.
- **Algorithm:** Random Forest Classifier
- **Dataset:** `train.csv`, `test.csv`
- **Key Points:**
  - Label encoding for categorical features
  - Evaluated using **recall**
  - Predictions outputted in structured CSV

---

### 5️⃣ Pistachio Classification
- **Goal:** Multi-class classification.
- **Algorithm:** K-Nearest Neighbors (KNN)
- **Dataset:** `train.csv`, `test.csv`
- **Key Points:**
  - Standardization of features
  - Train-test split for validation
  - Weighted F1-score used for evaluation
  - Predictions ready for submission

---

## 🛠 Tools & Libraries
- **Python**, **Pandas**, **NumPy**
- **Scikit-learn** (ML algorithms & preprocessing)
- **Matplotlib & Seaborn** (visualizations)

---

## 📁 Repository Structure
- bank_customers
- life_expectancy
- mall_customers
- mushroom_hunter
- pistachio
- README.md


---

## 🎯 Key Takeaways
- Preprocessing and scaling are critical for ML models
- Ensemble methods like Random Forest and AdaBoost improve classification performance
- Polynomial features can improve regression models
- Clustering reveals hidden patterns in unsupervised tasks

---

## 📌 How to Run

```bash
git clone <repo_url>
Install dependencies:

pip install pandas numpy scikit-learn matplotlib seaborn

Navigate to a project folder and run the corresponding script or notebook.
