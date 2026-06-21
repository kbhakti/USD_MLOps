# AAI-540 Final Project — Deliverables Checklist
## Group 6: Student Performance Prediction
## Last Updated: June 20, 2026

---

## Overview

There are **3 deliverables** due on Canvas (320 points total).
All files must be submitted **at the same time** by one team delegate.

**File naming convention:**
- `FinalProject_Team-6_Deliverable-1.pdf` — Design Document
- `FinalProject_Team-6_Deliverable-2.mp4` — Video Demo
- `FinalProject_Team-6_VideoScript.pdf` — Video Transcript
- GitHub repo link — included in Design Document

---

## Deliverable #1: Design Document (100 pts)

The design document draft already exists. It needs to be **updated with actual results** from the SageMaker run.

### Sections to update:

| Section | What to Add | Status |
|---|---|---|
| Problem Statement (1-2 paragraphs) | Already written | DONE |
| Impact Measurement (1-2 paragraphs) | Already written | DONE |
| Security Checklist | Already written | DONE |
| Data Sources | Add S3 bucket path: `sagemaker-us-east-1-882248517783/student-performance/` | NEEDS UPDATE |
| Data Engineering | Add: combined 2 CSVs, 1044 records, zero missing values, uploaded to S3 | NEEDS UPDATE |
| Feature Engineering | Add: binary encoded 13 features, one-hot encoded 5 features, StandardScaler on 13 numerical features, Feature Store with 1044 records | NEEDS UPDATE |
| Model Training & Evaluation | Add: 3 models trained (LR, DT, RF), GridSearchCV tuning, best params: max_depth=5, min_samples_leaf=2, n_estimators=100. Add actual accuracy/F1/AUC scores from Notebook 03 | NEEDS UPDATE |
| Model Deployment | Add: SageMaker endpoint (ml.t2.medium), batch transform completed, model artifact in S3, model registered in Model Registry | NEEDS UPDATE |
| Model Monitoring | Add: performance tracked over 10 windows, KS test for drift detection, alert system (accuracy>0.70, F1>0.65), Model Monitor baseline created | NEEDS UPDATE |
| CI/CD | Add: SageMaker Pipeline with 3 steps (DataProcessing → ModelTraining → RegisterModel), pipeline executed successfully | NEEDS UPDATE |
| GitHub Link | Add repo URL | NEEDS UPDATE |

### How to update:
1. Open the existing Design Document (PDF/Word)
2. Update each section above with 2-3 paragraphs describing actual findings
3. Add the GitHub repository link
4. Export as PDF
5. Name it: `FinalProject_Team-6_Deliverable-1.pdf`

---

## Deliverable #2: Video Demo (80 pts)

### Required elements to show in the video:

| Element | Where to Find It | Status |
|---|---|---|
| Business use case introduction | Verbal — see VIDEO_SCRIPT.md | NOT RECORDED |
| Architecture diagram | Verbal description of pipeline flow | NOT RECORDED |
| **Feature Store & feature groups** | Notebook 02, Section 2.9 — scroll to show feature group creation and record ingestion output | CODE DONE, NOT RECORDED |
| **Infrastructure monitoring dashboards** | Notebook 05, Section 5.1 — scroll to show 4-panel monitoring dashboard (Accuracy, F1, Precision, Recall over time) | CODE DONE, NOT RECORDED |
| **Model or data monitoring reports** | Notebook 05, Section 5.2 — scroll to show KS test drift table and distribution comparison plots. Section 5.3 — data quality report | CODE DONE, NOT RECORDED |
| **CI/CD DAG in successful state** | Notebook 05, Section 5.6 — scroll to show pipeline execution status with all steps "Succeeded" | CODE DONE, NOT RECORDED |
| **CI/CD DAG in failed state** | **NOT DONE** — see instructions below | NOT DONE |
| **Model Registry** | Notebook 03, Section 3.10 — scroll to show model_package_arn output | CODE DONE, NOT RECORDED |
| **Batch inference output** | Notebook 04, Section 4.4 — scroll to show batch transform output | CODE DONE, NOT RECORDED |
| **Endpoint invocation output** | Notebook 04, Section 4.3 — scroll to show predictions vs actual | CODE DONE, NOT RECORDED |
| Future improvements | Verbal — see VIDEO_SCRIPT.md | NOT RECORDED |
| Challenges and risks | Verbal — see VIDEO_SCRIPT.md | NOT RECORDED |
| Equal presentation by all members | Split into 3 parts in VIDEO_SCRIPT.md | NOT RECORDED |

### How to create the failed CI/CD state:
When you restart SageMaker to record the video, add a new cell in Notebook 05 and run:
```python
# Trigger a failed pipeline run with invalid input
failed_input = ParameterString(name='InputData', default_value='s3://invalid-bucket/no-data.csv')

pipeline_fail = Pipeline(
    name='StudentPerformancePipeline-FailTest',
    parameters=[failed_input],
    steps=[processing_step, training_step, register_step],
    sagemaker_session=session
)
pipeline_fail.upsert(role_arn=role)
execution_fail = pipeline_fail.start()
execution_fail.wait()
print(f'Status: {execution_fail.describe()["PipelineExecutionStatus"]}')

# Show failed steps
steps = execution_fail.list_steps()
for step in steps:
    print(f"{step['StepName']:30s} {step['StepStatus']}")
```
Screenshot the failed output for the video.

### Video format:
- 10-15 minutes total
- MP4 format
- Screencast with voice narration
- Each member presents ~4-5 minutes
- Submit with outline/transcript

### Files to submit:
1. `FinalProject_Team-6_Deliverable-2.mp4` — the video
2. `FinalProject_Team-6_VideoScript.pdf` — export VIDEO_SCRIPT.md as PDF

---

## Deliverable #3: Code — GitHub Repository (140 pts)

### 8 requirements checklist:

**Method (4 requirements):**

| # | Requirement | Status | Action Needed |
|---|---|---|---|
| 1 | Code stored in GitHub, clean and professional, notebooks in .ipynb | NOT DONE | Push to GitHub |
| 2 | Code is clean, has useful comments, project-focused | DONE | Already clean |
| 3 | Data stored in S3 and documented in GitHub | DONE (S3) | Add S3 paths to README |
| 4 | Charts/graphs included in .ipynb files | DONE | All notebooks have visualizations |

**ML Design (2 requirements):**

| # | Requirement | Status | Action Needed |
|---|---|---|---|
| 5 | Codebase is comprehensive and complete | DONE | 5 notebooks + source code |
| 6 | Codebase and design document mutually reinforcing | PARTIAL | Update design document with actual results |

**Teamwork (2 requirements):**

| # | Requirement | Status | Action Needed |
|---|---|---|---|
| 7 | All team members contribute to GitHub | NOT DONE | Each person must make at least 1 commit |
| 8 | Commit history available for review | NOT DONE | Need commits from all 3 members |

### How to push to GitHub:

**Option A: Use existing repo (kbhakti/USD_MLOps)**
```bash
git clone https://github.com/kbhakti/USD_MLOps.git
cd USD_MLOps
# Copy all project files into the repo
git add .
git commit -m "Add complete ML system - Student Performance Prediction"
git push
```

**Option B: Create new repo**
1. Go to github.com → New Repository
2. Name: `USD_MLOps` or `student-performance-mlops`
3. Make it Public
4. Clone and push all files

### Files to push to GitHub:
```
USD_MLOps/
├── README.md                          ← Create this
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── student-mat.csv
│   │   └── student-por.csv
│   └── processed/
│       └── (note: processed files generated by notebooks)
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_eda_feature_engineering.ipynb
│   ├── 03_model_training_evaluation.ipynb
│   ├── 04_model_deployment.ipynb
│   └── 05_monitoring_cicd.ipynb
└── src/
    ├── inference.py
    ├── train.py
    └── preprocessing.py
```

### How to ensure all 3 members have commits:
1. **Lokesh** pushes the initial codebase
2. **Bhakti** makes a commit — example: update README.md or add a comment in Notebook 03
3. **Sabina** makes a commit — example: update README.md or add a comment in Notebook 05

Each person clones the repo, makes a small change, commits with their own GitHub account, and pushes.

---

## Task Assignment

| Task | Assigned To | Deadline |
|---|---|---|
| Push code to GitHub | Lokesh | ASAP |
| Make a commit to GitHub | Bhakti | Before submission |
| Make a commit to GitHub | Sabina | Before submission |
| Update Design Document sections (Data Sources, Data Engineering, Feature Engineering) | Lokesh | Before submission |
| Update Design Document sections (Model Training, Deployment) | Bhakti | Before submission |
| Update Design Document sections (Monitoring, CI/CD) | Sabina | Before submission |
| Record video Part 1 (0:00-5:00) | Lokesh | Before submission |
| Record video Part 2 (5:00-10:00) | Bhakti | Before submission |
| Record video Part 3 (10:00-14:00) | Sabina | Before submission |
| Trigger failed CI/CD pipeline for video | Whoever records that section | During recording |
| Combine video + export as MP4 | Any member | Before submission |
| Submit all deliverables on Canvas | Team delegate | Before deadline |

---

## Submission Checklist (Final)

Before clicking "Submit Assignment" on Canvas, verify:

- [ ] Design Document exported as PDF with all sections updated
- [ ] Design Document includes GitHub repo link
- [ ] Video is 10-15 minutes, MP4 format
- [ ] Video shows ALL 6 required SageMaker components
- [ ] Video includes CI/CD in both successful AND failed state
- [ ] Video transcript/outline included
- [ ] Each team member presents equally in the video
- [ ] All files submitted AT THE SAME TIME on Canvas
- [ ] GitHub repo is public and accessible
- [ ] All 3 team members have commits in GitHub
- [ ] SageMaker notebook instance is STOPPED after recording
- [ ] SageMaker endpoint is DELETED
