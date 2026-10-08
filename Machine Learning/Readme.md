
# 🤖 Machine Learning

> **From understanding ML fundamentals to building, evaluating, and improving predictive models.**

This folder is the **Machine Learning stage** of my [AI/ML Engineering — The Build Log](../README.md).

Here I move beyond Python, NumPy, Pandas, and Data Visualization into actual Machine Learning — working with datasets, training models, evaluating performance, comparing algorithms, and experimenting with different approaches.

The goal is not just to make a model produce predictions.

The goal is to understand **why a model performs the way it does.**

---

## 🎯 What This Section Covers

- 🧠 Machine Learning fundamentals
- 📊 Exploratory Data Analysis
- 🧹 Data preprocessing
- 🔀 Train/Test splitting
- ⚙️ Feature engineering
- 📏 Feature scaling
- 🎯 Regression
- 🏷️ Classification
- 🌲 Tree-based models
- 🔍 Model evaluation
- 🔁 Cross-validation
- 🎛️ Hyperparameter tuning
- 🧪 Model experimentation
- 📈 Model comparison

---

# 🧠 Machine Learning Workflow

```text
              REAL-WORLD PROBLEM
                       │
                       ▼
                     DATA
                       │
                       ▼
              DATA UNDERSTANDING
                       │
                       ▼
                     EDA
                       │
                       ▼
              DATA PREPROCESSING
                       │
                       ▼
              FEATURE ENGINEERING
                       │
                       ▼
                TRAIN / TEST SPLIT
                       │
                       ▼
                 MODEL TRAINING
                       │
                       ▼
                MODEL EVALUATION
                       │
                       ▼
             HYPERPARAMETER TUNING
                       │
                       ▼
                MODEL COMPARISON
                       │
                       ▼
                  FINAL MODEL
```

---

# 📂 Notebooks & Experiments

## ❤️ `Heart_Project.ipynb`

A Machine Learning project using the heart disease dataset.

### Focus

- Data exploration
- Data preprocessing
- Feature analysis
- Classification
- Model training
- Model evaluation
- Prediction

**Dataset:** `heart.csv`

---

## 🏥 `Health.ipynb`

A Machine Learning experiment focused on health-related prediction.

### Concepts

- Data preprocessing
- Feature selection
- Classification
- Model training
- Model evaluation
- Prediction

---

## 🏦 `Insurance.ipynb`

A Machine Learning experiment based on insurance data.

**Dataset:** `insurance.csv`

### Focus

- Dataset understanding
- Exploratory Data Analysis
- Feature preprocessing
- Regression
- Model training
- Model evaluation

---

## 🚢 `TitanicModels.ipynb`

A classification experiment using the Titanic dataset.

The objective is to predict passenger survival based on available passenger information.

### Concepts

- Data cleaning
- Missing-value handling
- Categorical feature processing
- Feature engineering
- Classification
- Model evaluation
- Model comparison

---

## 🎛️ `GridSearchCV.ipynb`

A dedicated experiment focused on **hyperparameter optimization** using `GridSearchCV`.

### Concepts

- Parameters vs hyperparameters
- Cross-validation
- Parameter grids
- Model selection
- Systematic hyperparameter search
- Performance comparison

The goal is to understand how models can be systematically optimized instead of manually guessing parameter values.

---

# 📊 Datasets

| Dataset | Purpose |
|---|---|
| `heart.csv` | Heart disease prediction |
| `insurance.csv` | Insurance prediction / regression |
| `Student Social Media And Mental Health Impact.csv` | Student behavior and mental-health-related ML experiments |

---

# 🧹 Data Preprocessing

Preparing raw data before model training.

### Topics

- Missing values
- Duplicate values
- Data types
- Numerical variables
- Categorical variables
- Encoding
- Feature scaling
- Data cleaning
- Train/Test splitting
- Preventing data leakage

---

# 📊 Exploratory Data Analysis

Before training a model, I analyze the dataset to understand:

- Feature distributions
- Relationships between features
- Correlations
- Outliers
- Missing values
- Class distributions
- Feature-target relationships

> **A model is only as useful as the understanding behind the data it receives.**

---

# ⚙️ Feature Engineering

Transforming raw variables into representations that are more useful for Machine Learning models.

### Topics

- Feature creation
- Feature transformation
- Encoding
- Scaling
- Feature selection
- Handling skewed variables
- Feature importance
- Interaction features

---

# 🎯 Supervised Learning

The primary focus of these experiments is **Supervised Learning**.

## Regression

Used when the target variable is continuous.

### Algorithms

- Linear Regression
- Polynomial Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regression
- Random Forest Regression

### Metrics

- MAE
- MSE
- RMSE
- R²

---

# 🏷️ Classification

Used when the target represents a class or category.

### Algorithms

- Logistic Regression
- K-Nearest Neighbors
- Decision Trees
- Random Forest
- Support Vector Machines
- Naive Bayes

### Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC

---

# 🌲 Tree-Based & Ensemble Learning

Exploring models that use decision trees and combinations of multiple models.

### Topics

- Decision Trees
- Random Forest
- Bagging
- Boosting
- Gradient Boosting
- Ensemble learning
- Feature importance

---

# 🔁 Cross-Validation

Cross-validation provides a more reliable estimate of model performance than relying on a single train/test split.

```text
Dataset
   │
   ├── Fold 1 → Train / Validation
   ├── Fold 2 → Train / Validation
   ├── Fold 3 → Train / Validation
   ├── Fold 4 → Train / Validation
   └── Fold 5 → Train / Validation
                │
                ▼
        Average Performance
```

This is especially useful when comparing multiple models.

---

# 🎛️ Hyperparameter Tuning

Model performance can depend heavily on the choice of hyperparameters.

```text
Model
  ↓
Parameter Grid
  ↓
Cross Validation
  ↓
GridSearchCV
  ↓
Best Parameters
  ↓
Optimized Model
```

### Topics

- Hyperparameters vs parameters
- Grid Search
- Random Search
- Cross-validation
- Parameter selection
- Model optimization

---

# 📈 Model Evaluation

A model should never be judged only by whether it produces predictions.

## Classification

```text
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
ROC-AUC
```

## Regression

```text
MAE
MSE
RMSE
R²
```

The objective is to understand:

> **Which model performs best, why it performs best, and where it fails.**

---

# 🧪 Learning Through Experiments

This folder is intentionally experimental.

The workflow is:

```text
Learn
  ↓
Understand
  ↓
Implement
  ↓
Experiment
  ↓
Evaluate
  ↓
Debug
  ↓
Improve
  ↓
Repeat
```

Not every experiment is expected to produce the best possible model.

The important part is understanding **what changed and why.**

---

# 🧠 Engineering Questions

While working through these notebooks, I am learning to ask:

- Why is this algorithm suitable for this problem?
- What assumptions does the model make?
- Is the dataset balanced?
- Is there data leakage?
- Are the features useful?
- Should the data be scaled?
- Which evaluation metric actually matters?
- Is the model overfitting?
- Would cross-validation provide a better estimate?
- Can hyperparameter tuning improve the model?
- Why did one model outperform another?
- Where does the model fail?

---

# 🛠️ Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

# 📁 Folder Structure

```text
Machine Learning/
│
├── 📓 GridSearchCV.ipynb
├── 📓 Health.ipynb
├── 📓 Heart_Project.ipynb
├── 📓 Insurance.ipynb
├── 📓 TitanicModels.ipynb
│
├── 📊 Student Social Media And Mental Health Impact.csv
├── 📊 heart.csv
├── 📊 insurance.csv
│
└── 📖 README.md
```

---

# 🚀 What's Next?

The Machine Learning track will continue toward:

```text
Machine Learning
      │
      ▼
Advanced Feature Engineering
      │
      ▼
Ensemble Learning
      │
      ▼
Model Optimization
      │
      ▼
ML Pipelines
      │
      ▼
Model Deployment
      │
      ▼
Deep Learning
```

The long-term objective is to move from **training individual models** to building complete, reliable Machine Learning systems.

---

# 🔗 Parent Repository

This folder is part of:

## ⚡ AI/ML Engineering — The Build Log

The complete repository covers the progression from:

```text
Python
  ↓
NumPy
  ↓
Pandas
  ↓
Data Visualization
  ↓
Machine Learning
  ↓
Deep Learning
  ↓
Computer Vision
  ↓
NLP
  ↓
Generative AI
  ↓
AI Engineering
```
