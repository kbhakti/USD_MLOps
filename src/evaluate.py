import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib


def evaluate(model_path, test_path, output_path):
    model = joblib.load(model_path)
    df = pd.read_csv(test_path)

    X = df.drop(columns=['performance'])
    y = df['performance']

    predictions = model.predict(X)
    probabilities = model.predict_proba(X)[:, 1]

    metrics = {
        'accuracy': accuracy_score(y, predictions),
        'precision': precision_score(y, predictions),
        'recall': recall_score(y, predictions),
        'f1_score': f1_score(y, predictions),
        'auc_roc': roc_auc_score(y, probabilities)
    }

    os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, 'evaluation_metrics.json'), 'w') as f:
        json.dump(metrics, f, indent=2)

    print('Evaluation Metrics:')
    for k, v in metrics.items():
        print(f'  {k}: {v:.4f}')

    return metrics


if __name__ == '__main__':
    evaluate(
        model_path=os.environ.get('MODEL_PATH', '../models/random_forest_best.joblib'),
        test_path=os.environ.get('TEST_PATH', '../data/processed/test.csv'),
        output_path=os.environ.get('OUTPUT_PATH', '../data/processed')
    )
