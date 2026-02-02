## 🌲 Classification Project Using Random Forest

This project implements a **supervised machine learning classification pipeline** using the **Random Forest algorithm**.  
The goal is to train a model on labeled data, evaluate its performance, and generate predictions for unseen test data.

---

## 📂 Dataset Overview

- **Training Data**: `train.csv`
- **Test Data**: `test.csv`
- **Target Column**: `class`
- **Features**: All remaining categorical attributes

The dataset is structured for a **binary classification** task.

---

## 🧩 Project Workflow

The workflow follows a standard machine learning pipeline:

---

## 1️⃣ Data Loading
- Load training and test datasets using **Pandas**
- Separate features and target labels from the training data

---

## 2️⃣ Data Preprocessing
- Apply **Label Encoding** to transform categorical features into numeric format
- Ensure consistent encoding across training, validation, and test sets

Why label encoding?  
> Random Forest requires numerical inputs, so categorical values must be converted.

---

## 3️⃣ Train–Test Split
- Split the training data into:
  - **80% training**
  - **20% validation**
- Helps evaluate model performance on unseen data

---

## 4️⃣ Model Training (Random Forest)
- Algorithm: **Random Forest Classifier**
- Default parameters used (can be tuned for better performance)
- Model trained on preprocessed training set

---

## 5️⃣ Model Evaluation
- Generate predictions on the validation set
- Evaluate using **Recall Score**  
  - Example: `Recall ≈ 1.0` for positive class `'p'`

---

## 6️⃣ Test Data Prediction
- Apply the trained model to the unseen test dataset
- Store predictions in a structured **DataFrame**
- Output ready for submission or further analysis

---

## 🛠️ Tools & Technologies

- **Programming Language**: Python
- **Data Handling**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (RandomForestClassifier)
- **Preprocessing**: LabelEncoder, Train-Test Split

---

## 🎯 Conclusion

This project demonstrates a complete **classification workflow**, including:
- Categorical feature encoding
- Model training with Random Forest
- Evaluation using recall score
- Prediction on unseen data

It highlights the suitability of ensemble methods like Random Forest for **categorical, small-to-medium-sized datasets**.

