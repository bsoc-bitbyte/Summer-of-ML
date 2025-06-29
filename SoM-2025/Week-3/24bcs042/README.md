# Week 3 - SA-2025 GRADED ASSIGNMENT 🚀

## 📁 Project Title: Spaceship Titanic - Alternate Dimension Prediction

This is a machine learning project built around the **Spaceship Titanic** dataset from Kaggle. The objective is to predict which passengers were teleported to another dimension during a cosmic event. The task uses various classification models, primarily focusing on **Support Vector Machines (SVM)**.

## 📊 Dataset

- **Source**: [Google Drive CSV](https://drive.google.com/file/d/1sbQ5WJ-KCPBrhT2YagtaARGoujCMpB8Q/view)
- **Records**: ~13,000 passengers
- **Features**: Includes passenger ID, home planet, cryo-sleep status, destination, cabin, age, and more.
- **Target**: `Transported` (Binary: True/False)

---

## 🎯 Objective

Build a classification model to accurately predict if a passenger was **transported** to an alternate dimension.

---

## ⚙️ Technologies Used

- Python
- Jupyter Notebook
- Libraries:
  - `pandas`, `numpy`, `matplotlib`,`sneaborn`
  - `scikit-learn`

---

## 🧠 Machine Learning Techniques

- **Preprocessing**:
  - Handling missing values
  - Label encoding
  - Feature scaling (`StandardScaler`)
- **Model Used**: Support Vector Machine (SVM)
- **Evaluation Metrics**:
  - Accuracy
  - ROC-AUC
  - Cross-validation
  - Classification report

---

## 📈 Model Performance (Logistic Regression)

| Metric            | Value                  |
|-------------------|------------------------|
| Accuracy          | `~0.78`                |
| ROC-AUC Score     | `~0.87`                |
| Cross-Validation  | `[0.78619756 0.79364005 0.76792963 0.80175913 0.7731889 ]` (cv=5) |
| F1-Score (Class 0) | 0.78                   |
| F1-Score (Class 1) | 0.78                   |



## 📈 Model Performance (SVM)

| Metric            | Value                  |
|-------------------|------------------------|
| Accuracy          | `~0.78`                |
| ROC-AUC Score     | `~0.84`                |
| Cross-Validation  | `[0.78619756 0.79364005 0.76792963 0.80175913 0.7731889 ]` (cv=5) |
| F1-Score (Class 0) | 0.76                   |
| F1-Score (Class 1) | 0.81                   |

---