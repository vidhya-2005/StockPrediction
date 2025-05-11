# 📈 Stock Profit Prediction App

This project builds a machine learning system to predict whether a financial portfolio will yield a **positive or negative profit** based on historical financial data (2011–2024). It includes exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment via a Streamlit web app.

---

## 🔍 Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Results](#results)
- [Deployment](#deployment)
- [Usage](#usage)
- [Limitations](#limitations)
- [Future Scope](#future-scope)
- [File Structure](#file-structure)


---

## 🚀 Project Overview

The goal is to predict whether the **Total Profit (`Total`)** of a portfolio is **positive or negative**, using financial indicators like `Total Equity`, `World Equity`, and `Total Bond`.

- Built in Jupyter Notebook (`Stock_Prediction.ipynb`)
- Deployed via Streamlit (`app.py`)
- Best model: **RandomForestClassifier** with 0.97 accuracy

---

## 📊 Dataset

The dataset (`stock_data.csv`) includes **159 rows** and these columns:

- `Date`: Record date (2011–2024)
- `Total Equity`, `Domestic Equity`, `World Equity`: Equity values
- `Hybrid`: Mixed asset metric
- `Total Bond`, `Taxable Bond`, `Municipal Bond`: Bond values
- `Total`: Net portfolio profit/loss

### Sample Data

| Date       | Total Equity | World Equity | Total Bond | Total     |
|------------|--------------|--------------|------------|-----------|
| 2011-10-05 | -4002        | 497          | -5828      | -11184.0  |
| 2011-10-12 | -7397        | -1555        | 3954       | -2931.0   |

---

## 🔧 Workflow

### 1. Exploratory Data Analysis (EDA)
- Histograms, boxplots, correlation heatmaps
- Time-series trend analysis

### 2. Feature Engineering
- Created features: `Year`, `Month`, `Total_lag1`, `Total_MA7`, `Equity_Bond_Ratio`
- Standardized features using `StandardScaler`

### 3. Model Training
- **Logistic Regression** (baseline)
- **RandomForestClassifier** (best performance)
- **TensorFlow Neural Network**

### 4. Evaluation Metrics
- Accuracy, F1-Score, ROC-AUC
- Confusion matrix visualization

---

## 📈 Results

| Model            | Accuracy | F1-Score | ROC-AUC |
|------------------|----------|----------|---------|
| Logistic         | 0.94     | 0.00     | 0.58    |
| RandomForest     | 0.97     | 0.67     | 0.97    |
| Neural Network   | 0.94     | 0.00     | 0.85    |

### Key Insights:
- RandomForest performed best due to robustness with non-linear patterns
- Low F1-Scores indicate class imbalance (positive vs. negative labels)

---

## 🌐 Deployment

The model is deployed via a **Streamlit app**.

### Sample Prediction:
- **Input**: `Total Equity = 1000`, `World Equity = 500`, `Total Bond = 200`
- **Output**: `Prediction: Positive (Prob: 0.82)`

## ▶️ Usage

### 📓 Jupyter Notebook

* Open `Stock_Prediction.ipynb` to view EDA, modeling, and evaluation
* You can generate `classifier.pkl` from this notebook

### 🚀 Streamlit App

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) to access the web app.

### 🌍 Streamlit Cloud

* In Streamlit Cloud, link the repo, set `app.py` as the entry point
* Deploy and access the generated URL: https://cool-pugs-grab.loca.lt

---

## ⚠️ Limitations

* Small dataset (159 rows) limits generalizability
* Class imbalance affects F1-score
* Streamlit app uses only 3 features, lacks temporal modeling

---

## 🔮 Future Scope

* Integrate APIs (e.g., Yahoo Finance) for real-time dynamic datasets
* Implement LSTM or Transformer-based time-series models
* Add SHAP explanations, user-friendly visualizations, and feature customization in the UI

---

## 📁 File Structure

```
stock-prediction-app/
├── Stock_Prediction.ipynb     # Main notebook
├── app.py                     # Streamlit app
├── stock_data.csv             # Dataset
├── README.md                  # Documentation
```

---

> *Made with ❤️ using Python, scikit-learn, TensorFlow & Streamlit.*
