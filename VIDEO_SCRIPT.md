# Video Script — AAI-540 Final Project
## Group 6: Student Performance Prediction
## Total Duration: 12-14 minutes

---

## LOKESH — Part 1 (0:00 - 5:00)

### Introduction (0:00 - 1:00)

"Hello everyone. We are Group 6 from AAI-540 — I am Lokesh, and my teammates are Bhakti and Sabina."

"Our project is Student Performance Prediction using Machine Learning and MLOps on AWS SageMaker."

"The problem we are solving is this — educational institutions struggle to identify students who need academic support before their grades drop. Traditional methods are reactive, meaning teachers only intervene after poor results are already observed."

"Our solution uses Machine Learning to predict whether a student will achieve High or Low academic performance based on historical and behavioral data — things like study time, attendance, parental education, and extracurricular activities. By providing early predictions, educators can offer timely support to at-risk students."

"We implemented this as a complete end-to-end MLOps system on AWS SageMaker. Let me walk you through the architecture."

"Our pipeline flows like this — data from Kaggle is stored in S3, processed through our preprocessing pipeline, analyzed with EDA, used to train models, the best model is deployed as an endpoint, and we have monitoring and CI/CD in place."

---

### Data Ingestion — Notebook 01 (1:00 - 2:30)

[SCREEN: Open Notebook 01, scroll to data loading cell]

"Starting with data ingestion. We used the UCI Student Performance dataset, sourced from Kaggle. It contains two CSV files — student-mat.csv with 395 Math students, and student-por.csv with 649 Portuguese language students. Each file has 33 features covering demographics, academic history, study habits, and family background."

[SCREEN: Scroll to show shape outputs]

"We performed thorough data quality checks. As you can see, there are zero missing values across all 33 columns in both datasets, and zero duplicate rows."

[SCREEN: Scroll to show missing values and duplicates output]

"We combined both datasets into a single dataframe of 1044 records and added a subject column to track the source. Then we created our binary target variable called performance — students with a final grade G3 of 12 or above are labeled as High Performance, and below 12 as Low Performance."

[SCREEN: Scroll to show target distribution]

"The classes are well balanced — 534 Low Performance and 510 High Performance students. This is important because it means we do not need to apply oversampling or undersampling techniques."

"Finally, we uploaded all raw and processed data to our S3 bucket for SageMaker access."

[SCREEN: Scroll to show S3 upload output]

---

### EDA & Feature Engineering — Notebook 02 (2:30 - 5:00)

[SCREEN: Open Notebook 02, scroll to target distribution chart]

"Moving to Exploratory Data Analysis. This histogram shows the distribution of final grades. The red dashed line at 12 is our classification threshold. You can see the bar chart confirms our balanced class split."

[SCREEN: Scroll to numerical distributions]

"We analyzed distributions for all numerical features. Most features like age, study time, and parental education follow expected patterns."

[SCREEN: Scroll to correlation heatmap]

"This correlation heatmap is very important. Notice that G1 and G2 — the first and second period grades — have correlations above 0.8 with the final grade G3. If we included these as features, our model would essentially be cheating by using future information. So we dropped G1, G2, and G3 from the feature set to prevent data leakage."

[SCREEN: Scroll to feature vs target boxplots]

"These boxplots show how key features relate to performance. Students with fewer failures, more study time, and higher parental education levels tend to perform better. Alcohol consumption — both weekday and weekend — shows a negative impact on grades."

[SCREEN: Scroll to categorical analysis]

"Looking at categorical features, students who aspire to higher education show significantly better performance. Urban students slightly outperform rural students."

[SCREEN: Scroll to encoding and scaling]

"For feature engineering, we binary encoded 13 yes/no features, applied one-hot encoding to 5 multi-class features like mother's job, father's job, and school reason, and used StandardScaler on 13 numerical features. The final processed dataset has 41 columns."

[SCREEN: Scroll to Feature Store output]

"We ingested all 1044 processed records into a SageMaker Feature Store feature group. This provides a centralized, versioned store for our features that can be reused across training and inference."

"Now I will hand it over to Bhakti who will cover model training and deployment."

---

## BHAKTI — Part 2 (5:00 - 10:00)

### Model Training & Evaluation — Notebook 03 (5:00 - 8:00)

[SCREEN: Open Notebook 03, scroll to data split]

"Thank you Lokesh. I am Bhakti, and I will walk through our model training, evaluation, and deployment."

"We split the processed data into three sets using stratified sampling to maintain class balance — 70 percent for training with 730 samples, 15 percent for validation with 157 samples, and 15 percent for testing with 157 samples."

[SCREEN: Scroll to Logistic Regression results]

"We trained three supervised classification models. First, Logistic Regression — a linear baseline model. It achieved a validation accuracy of approximately 71 percent."

[SCREEN: Scroll to Decision Tree results]

"Second, a Decision Tree classifier. This model overfits the training data with 100 percent training accuracy but only around 62 percent on validation, showing it memorized the training patterns."

[SCREEN: Scroll to Random Forest results]

"Third, a Random Forest classifier with 100 trees. This performed between the other two models on validation."

[SCREEN: Scroll to model comparison table]

"This comparison table shows all five metrics side by side. Logistic Regression and Random Forest are close competitors, both significantly outperforming the Decision Tree."

[SCREEN: Scroll to comparison bar chart]

"The bar chart makes the differences more visible."

[SCREEN: Scroll to confusion matrices]

"The confusion matrices show the breakdown of correct and incorrect predictions for each model. The Decision Tree makes the most errors overall."

[SCREEN: Scroll to ROC curves]

"The ROC curves confirm that Logistic Regression and Random Forest have the best discrimination ability, with AUC scores around 0.77 to 0.78."

[SCREEN: Scroll to hyperparameter tuning]

"We performed hyperparameter tuning on Random Forest using GridSearchCV with 5-fold cross-validation. We searched across number of estimators, max depth, minimum samples split, and minimum samples leaf. The best configuration was 100 estimators with max depth of 5 and minimum samples leaf of 2."

[SCREEN: Scroll to tuned model results]

"The tuned Random Forest achieved improved and stable performance across all metrics."

[SCREEN: Scroll to feature importance]

"This feature importance chart from the tuned Random Forest shows the top 20 most influential features. Failures, absences, desire for higher education, study time, and mother's education are the strongest predictors of student performance."

[SCREEN: Scroll to test set evaluation]

"On the held-out test set, our final model achieves the results shown here with the confusion matrix."

[SCREEN: Scroll to model registry output]

"We saved all three models and registered the best model in SageMaker Model Registry under the StudentPerformanceModelGroup with Approved status."

---

### Model Deployment — Notebook 04 (8:00 - 10:00)

[SCREEN: Open Notebook 04, scroll to endpoint deployment]

"For deployment, we packaged the model as a model.tar.gz artifact and deployed it as a SageMaker real-time endpoint on an ml.t2.medium instance."

[SCREEN: Scroll to endpoint invocation results]

"We tested the endpoint by sending 10 sample student records. Here you can see the predictions alongside the actual labels. The model correctly predicts most cases."

[SCREEN: Scroll to batch transform output]

"We also ran a SageMaker Batch Transform job, which processes the entire test set at once. This is useful for generating predictions on large datasets without maintaining a live endpoint. The batch output was saved to S3."

[SCREEN: Scroll to cleanup section]

"After validating the endpoint and batch transform, we deleted the endpoint to avoid ongoing charges. The model artifact remains in S3 and Model Registry for future redeployment."

"Now Sabina will cover monitoring and our CI/CD pipeline."

---

## SABINA — Part 3 (10:00 - 14:00)

### Monitoring & CI/CD — Notebook 05 (10:00 - 13:00)

[SCREEN: Open Notebook 05, scroll to performance monitoring]

"Thank you Bhakti. I am Sabina, and I will present our model monitoring, data drift detection, and CI/CD pipeline."

"Model monitoring is critical in production to ensure the model continues to perform well over time. We simulated monitoring by evaluating our model across 10 time windows, representing weekly batches of incoming data."

[SCREEN: Scroll to monitoring dashboard — 4 charts]

"This monitoring dashboard shows four key metrics over time — Accuracy, F1-Score, Precision, and Recall. The solid line shows the metric value for each week, the dashed gray line is the overall mean, and the shaded band represents one standard deviation. All metrics remain relatively stable, indicating no significant degradation."

[SCREEN: Scroll to data drift table]

"For data drift detection, we applied the Kolmogorov-Smirnov statistical test to compare the distribution of each numerical feature between our training data and new test data. The table shows the KS statistic, p-value, and whether drift was detected at the 0.05 significance level for all 13 features."

[SCREEN: Scroll to drift distribution plots]

"These side-by-side distribution plots visually confirm the drift analysis. The blue histograms represent training data and red represents test data. For most features, the distributions closely overlap, indicating no significant drift."

[SCREEN: Scroll to data quality report]

"Our data quality report verifies zero missing values across all features, with proper data types and expected value ranges."

[SCREEN: Scroll to alert system output]

"We implemented an automated alert system with two thresholds — Accuracy must stay above 0.70 and F1-Score above 0.65. Each monitoring window is checked and flagged as OK or ALERT. As you can see, the system identifies any windows where performance dips below acceptable levels."

[SCREEN: Scroll to Model Monitor output]

"We also created a SageMaker Model Monitor baseline using our training data. This baseline captures the statistical properties of our features — means, standard deviations, and distributions. In production, new incoming data would be compared against this baseline to automatically detect anomalies and drift."

[SCREEN: Scroll to pipeline creation]

"Finally, for CI/CD, we built a SageMaker Pipeline — this is our automated machine learning workflow. The pipeline consists of three steps."

"Step 1: Data Processing — using an SKLearn Processor to clean and split the data."

"Step 2: Model Training — using an SKLearn Estimator to train the Random Forest model."

"Step 3: Model Registration — automatically registering the trained model in the Model Registry if it meets quality standards."

[SCREEN: Scroll to pipeline execution output]

"The pipeline was created and executed successfully. All three steps completed with a Succeeded status, which represents a successful CI/CD run."

"In a production environment, this pipeline could be triggered automatically whenever new data arrives, or on a scheduled basis, ensuring the model stays up to date."

---

### Future Improvements & Challenges (13:00 - 14:00)

"Looking ahead, there are several ways we could enhance this system."

"First, we would build a real-time prediction and monitoring system that processes live academic data streams, generates continuous predictions, and sends early alert notifications for students who may need academic support."

"Second, we would integrate explainability tools like SHAP or LIME. These would help educators understand exactly why a student is predicted as at-risk — for example, whether it is due to high absences, low study time, or parental education factors. Transparency is essential for building trust in AI-driven decisions."

"Third, we would expand to larger and more diverse datasets from multiple educational institutions and regions. This would improve model generalization and reduce potential biases related to demographics or socioeconomic factors."

"Some challenges we faced during this project include AWS Academy budget limitations which required us to create a personal AWS account, working with a relatively small dataset of approximately 1000 records, and balancing model complexity with interpretability for a non-technical audience of educators."

"Despite these challenges, we successfully demonstrated a complete end-to-end MLOps workflow — from data ingestion and feature engineering, through model training and deployment, to monitoring and CI/CD — all on AWS SageMaker."

"Thank you for watching our presentation. We welcome any questions."

---

## END OF SCRIPT
