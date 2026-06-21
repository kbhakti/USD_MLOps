# Video Presentation Guide
## AAI-540 Final Project — Group 6: Student Performance Prediction

**Video Length:** 10-15 minutes
**Format:** MP4 with screencast + voice narration
**Requirement:** Each team member presents an equal portion

---

## Before Recording

### Step 1: Restart SageMaker Notebook Instance
1. Go to AWS Console → SageMaker → Notebook instances
2. Select `student-performance` → Actions → **Start**
3. Wait for status to change to **InService** (3-5 minutes)
4. Click **Open Jupyter**
5. All notebook outputs will still be saved — just open and scroll

### Step 2: Set Up Recording
- Use **Zoom** (start a solo meeting, share screen, hit Record)
- Or use **Screencast-O-Matic** / **QuickTime** (Mac) / **OBS Studio** (free)
- Make sure microphone is working and audio is clear
- Close unnecessary browser tabs and notifications

### Step 3: Prepare
- Have this guide open on a second screen or printed
- Practice your section once before recording
- Speak clearly and at a moderate pace

---

## Presentation Script

---

### PERSON 1: Lokesh — Minutes 0:00 to 5:00
**Topic: Business Context + Data Ingestion + EDA**

#### Slide/Intro (0:00 - 1:00)
Say:
> "Hello, we are Group 6 — Bhakti, Sabina, and Lokesh. Our project is Student Performance Prediction using Machine Learning."
>
> "The goal is to predict whether a student will achieve High or Low academic performance based on factors like study time, attendance, parental education, and extracurricular activities."
>
> "This helps educators identify at-risk students early so they can provide timely support."
>
> "We implemented this as an end-to-end MLOps system on AWS SageMaker."

#### Open Notebook 01 — Data Ingestion (1:00 - 2:30)
Scroll through and narrate:
> "We used the UCI Student Performance dataset from Kaggle. It contains two files — Math students with 395 records and Portuguese students with 649 records."
>
> [Show the data loading cells and shape outputs]
>
> "We performed data quality checks — there are zero missing values and zero duplicate rows."
>
> [Show missing values output]
>
> "We combined both datasets into 1044 total records and created a binary target variable. Students with a final grade of 12 or above are classified as High Performance, and below 12 as Low Performance."
>
> [Show target distribution output]
>
> "The classes are well balanced — 534 Low and 510 High."
>
> "We uploaded all data to S3 for SageMaker access."
>
> [Show S3 upload output]

#### Open Notebook 02 — EDA (2:30 - 5:00)
Scroll through and narrate:
> "In our Exploratory Data Analysis, we first looked at the distribution of final grades."
>
> [Show the G3 histogram and target distribution bar chart]
>
> "We analyzed all numerical and categorical features."
>
> [Show distribution plots]
>
> "The correlation heatmap reveals that G1 and G2 — the first and second period grades — are highly correlated with the final grade G3, over 0.8. We dropped these to avoid data leakage in our model."
>
> [Show correlation heatmap]
>
> "Key findings: students with fewer failures, more study time, and higher parental education tend to perform better."
>
> [Show feature vs target boxplots]
>
> "For feature engineering, we binary encoded 13 features, one-hot encoded 5 multi-class features, and applied StandardScaler to 13 numerical features."
>
> "Finally, we ingested all processed data into SageMaker Feature Store."
>
> [Show Feature Store output — feature group created, records ingested]

---

### PERSON 2: Bhakti — Minutes 5:00 to 10:00
**Topic: Model Training + Evaluation + Deployment**

#### Open Notebook 03 — Model Training (5:00 - 8:00)
Scroll through and narrate:
> "We split the data into 70% training, 15% validation, and 15% test — maintaining class balance with stratified splitting."
>
> [Show split output]
>
> "We trained three models: Logistic Regression, Decision Tree, and Random Forest."
>
> [Show each model's training and validation accuracy]
>
> "Here is the model comparison table showing Accuracy, Precision, Recall, F1-Score, and AUC-ROC for all three models on the validation set."
>
> [Show comparison table and bar chart]
>
> "The confusion matrices show how each model classifies Low and High performance students."
>
> [Show confusion matrices]
>
> "The ROC curves confirm that Logistic Regression and Random Forest have the highest AUC."
>
> [Show ROC curves]
>
> "We performed hyperparameter tuning on Random Forest using GridSearchCV with 5-fold cross-validation. The best parameters were max_depth=5, min_samples_leaf=2, and 100 estimators."
>
> [Show best parameters output]
>
> "The top features driving predictions are failures, absences, desire for higher education, study time, and parental education."
>
> [Show feature importance chart]
>
> "We registered the best model in SageMaker Model Registry under the StudentPerformanceModelGroup."
>
> [Show model registry output]

#### Open Notebook 04 — Deployment (8:00 - 10:00)
Scroll through and narrate:
> "We deployed the best model as a SageMaker real-time endpoint using an ml.t2.medium instance."
>
> [Show endpoint deployment output]
>
> "We tested the endpoint by sending sample student data and receiving predictions."
>
> [Show endpoint invocation results — predictions vs actual]
>
> "We also ran a Batch Transform job for batch inference on the entire test set."
>
> [Show batch transform output]
>
> "After testing, we deleted the endpoint to avoid unnecessary charges."

---

### PERSON 3: Sabina — Minutes 10:00 to 14:00
**Topic: Monitoring + CI/CD + Future Work**

#### Open Notebook 05 — Monitoring & CI/CD (10:00 - 13:00)
Scroll through and narrate:
> "For model monitoring, we tracked performance metrics across simulated time windows to detect any degradation."
>
> [Show performance monitoring dashboard — 4 charts]
>
> "Our monitoring dashboard shows Accuracy, F1-Score, Precision, and Recall over 10 weeks. The shaded area represents one standard deviation from the mean."
>
> "We implemented a data drift detection system using the Kolmogorov-Smirnov statistical test on all 13 numerical features, comparing training and test distributions."
>
> [Show drift detection table]
>
> "The distribution comparison plots show how features like age, parental education, and study time compare between training and test data."
>
> [Show drift distribution plots]
>
> "We also built an alert system with thresholds — Accuracy above 0.70 and F1-Score above 0.65. Any window falling below these thresholds triggers an alert."
>
> [Show alert system output]
>
> "We created a SageMaker Model Monitor baseline from our training data for ongoing data quality monitoring."
>
> [Show Model Monitor output]
>
> "For CI/CD, we built a SageMaker Pipeline with three steps: Data Processing, Model Training, and Model Registration. The pipeline executed successfully."
>
> [Show pipeline creation and execution output]
>
> [Show pipeline steps status — all succeeded]

#### Future Improvements & Challenges (13:00 - 14:00)
Say:
> "For future improvements, we would consider:"
>
> "First, building a real-time prediction system that processes live academic data and sends early alerts for at-risk students."
>
> "Second, integrating explainability tools like SHAP or LIME to help educators understand which factors most influence predictions."
>
> "Third, expanding to larger and more diverse datasets from multiple institutions to improve generalization."
>
> "Some challenges we faced during development include AWS budget limitations, working with a relatively small dataset of about 1000 records, and balancing model complexity with interpretability."
>
> "Thank you for watching our presentation."

---

## After Recording

### Step 1: Stop SageMaker
1. Go to SageMaker Console → Notebook instances
2. Select `student-performance` → Actions → **Stop**
3. This is critical to avoid charges

### Step 2: Export Video
- Export as **MP4 format**
- Make sure total length is between 10-15 minutes
- File name: `FinalProject_Team-6_Deliverable-2.mp4`

### Step 3: Create Transcript
- Save this presentation guide as your outline/transcript
- File name: `FinalProject_Team-6_VideoScript.pdf`

### Step 4: Submit on Canvas
Submit all three deliverables **at the same time**:
1. `FinalProject_Team-6_Deliverable-1.pdf` — Design Document
2. `FinalProject_Team-6_Deliverable-2.mp4` — Video
3. `FinalProject_Team-6_VideoScript.pdf` — Video transcript/outline
4. GitHub repository link — include in design document

---

## Recording Tips

1. **Audio quality matters** — Use a headset or external microphone if possible. Record in a quiet room.

2. **Screen resolution** — Set your browser to 100% zoom so text is readable in the recording.

3. **Practice once** — Do a dry run of your section before the real recording. Time yourself.

4. **Scroll slowly** — When showing notebook outputs, scroll slowly so viewers can read the content.

5. **Highlight key outputs** — Click on important cells (charts, tables, metrics) and pause briefly while explaining.

6. **Edit out mistakes** — Use a video editor to cut out long pauses, restarts, or mistakes. Remove background noise.

7. **Transitions** — When switching presenters, briefly introduce the next person: "Now Bhakti will walk through the model training."

8. **Keep it professional** — This is a graduate-level presentation for business stakeholders.

9. **Time management** — Each person gets ~4-5 minutes. Don't go over 15 minutes total.

10. **Backup plan** — If SageMaker outputs don't show, take screenshots beforehand as backup slides.
