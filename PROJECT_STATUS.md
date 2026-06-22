# AAI-540 MLOps Final Project — Group 6
## Student Performance Prediction — Project Status

**Team:** Bhakti Kanungo, Sabina George, Lokesh Upputri
**Date:** June 20, 2026
**AWS Account:** Personal account (Lokesh - 882248517783, us-east-1)

---

## Project Overview

Predict student academic performance (High vs Low) using Machine Learning.
- **Dataset:** UCI Student Performance Dataset (Math: 395 + Portuguese: 649 = 1044 students)
  - Source: [UCI ML Repository](https://archive.ics.uci.edu/dataset/320/student+performance) — [direct download (zip)](https://archive.ics.uci.edu/static/public/320/student+performance.zip)
  - Citation: P. Cortez and A. Silva, "Using Data Mining to Predict Secondary School Student Performance," 2008.
- **Target:** Binary classification — High Performance (G3 >= 12) vs Low Performance (G3 < 12)
- **Best Model:** Tuned Random Forest Classifier
- **Platform:** AWS SageMaker

---

## Completed Components

### 1. Data Ingestion (Notebook 01)
- Loaded student-mat.csv (395 rows) and student-por.csv (649 rows)
- Data quality checks: zero missing values, zero duplicates
- Combined into single dataset (1044 rows, 35 columns)
- Created binary target variable: `performance`
- Uploaded raw and processed data to S3

### 2. EDA & Feature Engineering (Notebook 02)
- Distribution analysis for all numerical and categorical features
- Correlation heatmap — identified G1, G2 highly correlated with G3 (>0.8), dropped to avoid data leakage
- Feature vs target analysis (boxplots, crosstabs)
- Grade progression scatter plots
- Binary encoding for 13 categorical features
- One-hot encoding for 5 multi-class features (Mjob, Fjob, reason, guardian, subject)
- StandardScaler applied to 13 numerical features
- Final processed dataset: 1044 rows, 41 columns
- **SageMaker Feature Store:** Feature group created, 1044 records ingested

### 3. Model Training & Evaluation (Notebook 03)
- Data split: 70% train (730) / 15% validation (157) / 15% test (157)
- Three models trained:
  - Logistic Regression
  - Decision Tree
  - Random Forest
- Hyperparameter tuning via GridSearchCV (5-fold CV) on Random Forest
- Best parameters found: max_depth=5, min_samples_leaf=2, min_samples_split=2, n_estimators=100
- Model comparison with Accuracy, Precision, Recall, F1-Score, AUC-ROC
- Confusion matrices and ROC curves generated
- Feature importance analysis (top features: failures, absences, higher, studytime, Medu)
- Cross-validation performed for stability check
- All 3 models saved as .joblib files
- Model artifact (model.tar.gz) uploaded to S3
- **SageMaker Model Registry:** Best model registered in StudentPerformanceModelGroup

### 4. Model Deployment (Notebook 04)
- **Real-time Endpoint:** Deployed as `student-performance-endpoint` (ml.t2.medium)
- **Endpoint Invocation:** Tested with sample data, predictions returned successfully
- **Batch Transform:** Batch inference job completed, output saved to S3
- Endpoint deleted after testing to save costs

### 5. Monitoring & CI/CD (Notebook 05)
- **Performance Monitoring:** Tracked Accuracy, F1, Precision, Recall across 10 simulated time windows
- **Monitoring Dashboard:** 4 charts showing metric trends over time with mean and standard deviation bands
- **Data Drift Detection:** Kolmogorov-Smirnov test on all 13 numerical features (train vs test)
- **Data Drift Visualization:** Distribution comparison plots for key features
- **Data Quality Report:** Complete quality report for all features
- **Alert System:** Configured thresholds (Accuracy > 0.70, F1 > 0.65) with automated alerts
- **SageMaker Model Monitor:** Baseline created from training data
- **SageMaker Pipeline (CI/CD DAG):**
  - Step 1: DataProcessing (SKLearnProcessor)
  - Step 2: ModelTraining (SKLearn Estimator)
  - Step 3: RegisterModel (Model Registry)
  - Pipeline executed successfully

---

## AWS Resources Used

| Resource          | Details                            | Status               |
| ----------------- | ---------------------------------- | -------------------- |
| S3 Bucket         | sagemaker-us-east-1-882248517783   | Active (data stored) |
| Notebook Instance | student-performance (ml.t3.medium) | Stopped              |
| Feature Store     | student-performance-*              | Created              |
| Model Registry    | StudentPerformanceModelGroup       | Model registered     |
| Endpoint          | student-performance-endpoint       | Deleted              |
| Pipeline          | StudentPerformancePipeline         | Executed             |
| Model Monitor     | Baseline job                       | Completed            |

---

## Project File Structure

```
SageMaker/
├── data/
│   ├── raw/
│   │   ├── student-mat.csv
│   │   └── student-por.csv
│   └── processed/
│       ├── student_combined.csv
│       ├── student_processed.csv
│       ├── train.csv
│       ├── validation.csv
│       ├── test.csv
│       └── scaler.joblib
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_eda_feature_engineering.ipynb
│   ├── 03_model_training_evaluation.ipynb
│   ├── 04_model_deployment.ipynb
│   └── 05_monitoring_cicd.ipynb
├── src/
│   ├── inference.py
│   ├── train.py
│   └── preprocessing.py
├── models/
│   ├── logistic_regression.joblib
│   ├── decision_tree.joblib
│   ├── random_forest_best.joblib
│   └── model.tar.gz
└── requirements.txt
```

---

## Remaining Tasks

| Task                                     | Owner         | Estimated Time |
| ---------------------------------------- | ------------- | -------------- |
| Push code to GitHub (kbhakti/USD_MLOps)  | Lokesh/Bhakti | 10 min         |
| Record 10-15 min video demo              | All 3 members | 1-2 hours      |
| Finalize ML Design Document with results | All 3 members | 30 min         |
| Submit all 3 deliverables on Canvas      | Delegate      | 5 min          |
