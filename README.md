# 🩺 Breast Cancer Prediction Using Artificial Neural Networks (TensorFlow)

<div align="center">

### AI-Powered Breast Cancer Screening and Risk Assessment System

[🌐 Live Demo](https://breastcancerusinganns-sanjana.streamlit.app/) •
[📂 GitHub Repository](https://github.com/sanjanamali17/Breast_cancer_usingANNs)

</div>

---

## 📌 Project Overview

Breast cancer is one of the most common cancers affecting women worldwide. Early detection significantly improves treatment success rates and patient survival.

This project leverages **Artificial Neural Networks (ANNs)** built using **TensorFlow** to classify breast tumors as **Benign** or **Malignant** based on diagnostic measurements extracted from breast tissue images.

The system provides:

* Real-time tumor classification
* Prediction confidence score
* Medical risk interpretation
* Automated PDF report generation
* Interactive Streamlit web interface

The objective is to demonstrate how Artificial Intelligence can assist healthcare professionals in making faster and more informed diagnostic decisions.

> ⚠️ **Disclaimer:** This application is developed for educational and research purposes only. It is not intended to replace professional medical diagnosis, treatment, or healthcare advice.

---

# 🎯 Problem Statement

Breast cancer diagnosis often requires analyzing numerous medical measurements simultaneously.

Challenges include:

* Large number of diagnostic features
* Human interpretation variability
* Time-consuming manual assessment
* Need for rapid preliminary screening

Healthcare professionals can benefit from intelligent systems that assist in identifying high-risk cases early.

---

# 💡 Proposed Solution

This project introduces an AI-powered Breast Cancer Prediction System using a Deep Learning model based on Artificial Neural Networks.

The system:

✅ Accepts 30 medical diagnostic features

✅ Processes patient data using a trained ANN

✅ Predicts tumor type (Benign or Malignant)

✅ Provides confidence scores

✅ Generates structured diagnostic reports

✅ Supports clinical decision-making

The final diagnosis should always be performed by qualified healthcare professionals.

---

# 🧠 Artificial Neural Network Architecture

The model was developed using TensorFlow and Keras.

### Neural Network Pipeline

```text
Input Layer (30 Features)
          │
          ▼
Dense Hidden Layer
          │
          ▼
Dense Hidden Layer
          │
          ▼
Output Layer
          │
          ▼
Benign / Malignant Prediction
```

### Framework

* TensorFlow


### Learning Type

* Supervised Learning

### Problem Type

* Binary Classification

---

# 📊 Dataset Information

The project utilizes the Breast Cancer Wisconsin (Diagnostic) Dataset.

### Dataset Statistics

| Metric         | Value                 |
| -------------- | --------------------- |
| Total Samples  | 569                   |
| Features       | 30                    |
| Classes        | 2                     |
| Task Type      | Binary Classification |
| Missing Values | 0                     |

### Target Classes

| Class | Meaning   |
| ----- | --------- |
| 0     | Malignant |
| 1     | Benign    |

---

# 🔍 Exploratory Data Analysis

Comprehensive data analysis was performed before model development.

### Analysis Performed

* Feature Distribution Analysis
* Correlation Analysis
* Class Distribution Analysis
* Statistical Summary
* Feature Relationships

### Key Findings

* Several diagnostic features exhibit strong predictive power.
* Tumor radius, texture, perimeter, and area show significant influence.
* The dataset is well-structured and highly suitable for supervised learning.

---

# ⚙️ Machine Learning Pipeline

```text
Patient Data
      │
      ▼
Data Validation
      │
      ▼
Feature Preprocessing
      │
      ▼
Feature Scaling
      │
      ▼
Artificial Neural Network
      │
      ▼
Prediction
      │
      ▼
Confidence Score
      │
      ▼
Medical Report Generation
```

---

# 📈 Model Performance

## Final Results

| Metric              | Value                     |
| ------------------- | ------------------------- |
| Model Type          | Artificial Neural Network |
| Framework           | TensorFlow                |
| Classification Task | Binary                    |
| Accuracy            | ~97%                      |
| Dataset Size        | 569 Samples               |
| Features            | 30                        |

### Performance Highlights

✅ High Classification Accuracy

✅ Fast Prediction Time

✅ Strong Generalization

✅ Suitable for Decision Support Applications

---

# 🚀 Live Application

### Try the Model

👉 https://breastcancerusinganns-sanjana.streamlit.app/

### Features Available

* Interactive Prediction Interface
* Confidence Score Display
* Medical Risk Interpretation
* PDF Report Download
* Real-Time Classification

---

# 🛠️ Technology Stack

## Programming Language

* Python

## Deep Learning

* TensorFlow
* Keras

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib

## Web Application

* Streamlit

## Report Generation

* ReportLab

---

# 📂 Project Structure

```bash
Breast_cancer_usingANNs/
│
├── app.py
├── model.h5
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── model_training.ipynb
│
├── assets/
│   └── screenshots/
│
└── reports/
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/sanjanamali17/Breast_cancer_usingANNs.git
```

Navigate to project folder:

```bash
cd Breast_cancer_usingANNs
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# 📊 Project Metrics

| Metric                  | Achievement |
| ----------------------- | ----------- |
| Dataset Samples         | 569         |
| Medical Features        | 30          |
| Prediction Classes      | 2           |
| ANN Accuracy            | ~97%        |
| Deep Learning Framework | TensorFlow  |
| Deployment Platform     | Streamlit   |
| PDF Reports             | Supported   |
| Prediction Time         | < 1 Second  |

---

# 🎓 Skills Demonstrated

This project showcases expertise in:

* Deep Learning
* Artificial Neural Networks
* TensorFlow
* Healthcare AI
* Binary Classification
* Feature Engineering
* Data Analysis
* Model Evaluation
* Streamlit Deployment
* End-to-End AI Development

---

# 🔮 Future Enhancements

* Explainable AI (XAI)
* SHAP-Based Interpretability
* Medical Image Integration
* Multi-Class Tumor Classification
* Cloud Deployment
* Doctor Dashboard
* Patient History Tracking
* Electronic Health Record Integration

---

# 🌟 Why This Project Matters

Healthcare systems generate large volumes of diagnostic data that can be difficult to interpret efficiently.

By combining Deep Learning with medical diagnostics, this project demonstrates how AI can:

* Improve screening efficiency
* Reduce diagnostic workload
* Assist healthcare professionals
* Enable faster clinical decision-making
* Support early cancer detection initiatives

---

# 👩‍💻 Author

## Sanjana Mali

AI & Data Science Engineer

### Connect

GitHub: https://github.com/sanjanamali17

Live Demo:
https://breastcancerusinganns-sanjana.streamlit.app/

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

A star helps increase visibility and supports future AI and healthcare projects.
