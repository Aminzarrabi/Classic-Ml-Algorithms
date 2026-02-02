## 🛍️ Mall Customer Segmentation Using K-Means Clustering

This project implements an **unsupervised machine learning pipeline** to segment mall customers based on their demographics and spending behavior.  
The goal is to identify distinct customer groups for targeted marketing and business insights.

---

## 📂 Dataset Overview

- **Dataset**: `mall_customers.csv`
- **Features**:
  - `CustomerID` (dropped during preprocessing)
  - `Gender` (converted to numeric: Male=1, Female=0)
  - `Age`
  - `Annual Income (k$)`
  - `Spending Score (1-100)`

The dataset is suitable for **clustering analysis**.

---

## 🧩 Project Workflow

---

## 1️⃣ Data Preprocessing
- Gender is encoded numerically (`Male=1`, `Female=0`)
- `CustomerID` is removed as it is non-informative
- A reusable **Preprocessor class** was implemented to handle these transformations

---

## 2️⃣ Model Training (K-Means)
- Algorithm: **K-Means Clustering**
- Number of clusters: `5`
- Model is fitted on the processed data
- Predictions (cluster assignments) are saved for analysis and submission

---

## 3️⃣ Evaluation
- **Silhouette Score** is used to evaluate clustering quality
- Silhouette score scaled to 0–100 for easier interpretation
- Example: `sil_score_scaled = 100 * (sil_score + 1) / 2`

---

## 4️⃣ Visualization
- **Bar chart**: Number of customers in each segment
- **Histogram**: Distribution of `Spending Score (1-100)`
- These visualizations provide insight into cluster composition and spending behavior

---

## 🛠️ Tools & Technologies

- **Programming Language**: Python
- **Data Handling**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (KMeans, silhouette_score)
- **Visualization**: Matplotlib
- **Custom Preprocessing**: `Preprocessor` class

---

## 🎯 Conclusion

This project demonstrates a **full clustering workflow**, including:
- Data preprocessing and feature encoding
- Model training with K-Means
- Cluster evaluation using silhouette score
- Visualization of customer segments

It highlights how **unsupervised learning** can be applied to real-world business data for segmentation and strategy planning.

