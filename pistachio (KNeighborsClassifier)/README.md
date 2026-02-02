## 🤖 Classification Project Using K-Nearest Neighbors (KNN)

This project implements a **supervised machine learning classification pipeline** using the **K-Nearest Neighbors (KNN)** algorithm.  
The objective is to train a model on labeled data, evaluate its performance, and generate predictions on unseen test data.

---

## 📂 Dataset Overview

- **Training Data**: `train.csv`
- **Test Data**: `test.csv`
- **Target Column**: `Class`
- **Features**: All remaining numerical attributes

The dataset is structured for a **multi-class classification** task.

---

## 🧩 Project Workflow

The project follows a standard machine learning pipeline:

---

## 1️⃣ Data Loading
- Load training and test datasets using **Pandas**
- Separate features and target labels from the training data

---

## 2️⃣ Data Preprocessing
- Apply **Standardization** using `StandardScaler`
- Scale both training and test features to ensure:
  - Equal feature contribution
  - Improved distance-based model performance

Why scaling?
> KNN relies on distance metrics, so feature normalization is critical.

---

## 3️⃣ Train–Test Split
- Split the training data into:
  - **80% training**
  - **20% validation**
- Use a fixed `random_state` for reproducibility

---

## 4️⃣ Model Training (KNN)
- Algorithm: **K-Nearest Neighbors**
- Key parameters:
  - `n_neighbors = 95`
  - `p = 2` (Euclidean distance)
  - `weights = 'uniform'`

The model is trained using the processed training set.

---

## 5️⃣ Model Evaluation
- Generate predictions on the validation set
- Evaluate performance using:
  - **Weighted F1-score**

The weighted F1-score accounts for class imbalance and provides a reliable overall performance metric.

---

## 6️⃣ Test Data Prediction
- Apply the trained model to the unseen test dataset
- Store predictions in a structured **DataFrame**
- Output is ready for submission or further analysis

---

## 📊 Evaluation Metric

- **F1-score (weighted)**  
Chosen to balance precision and recall across all classes.

---

## 🛠️ Tools & Technologies

- **Programming Language**: Python
- **Data Handling**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Model**: K-Nearest Neighbors (KNN)
- **Preprocessing**: StandardScaler

---

## 🎯 Conclusion

This project demonstrates a complete **classification workflow**, including:
- Data preprocessing
- Feature scaling
- Model training and evaluation
- Prediction on unseen data

It highlights the importance of preprocessing when working with **distance-based algorithms** and provides a clean, reproducible machine learning pipeline.

