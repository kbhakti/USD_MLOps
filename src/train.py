import argparse
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import joblib


def train(args):
    train_path = os.path.join(args.train, 'train.csv')
    df = pd.read_csv(train_path)

    X = df.drop(columns=['performance'])
    y = df['performance']

    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        random_state=args.random_state
    )
    model.fit(X, y)

    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    f1 = f1_score(y, predictions)
    print(f'Training Accuracy: {accuracy:.4f}')
    print(f'Training F1-Score: {f1:.4f}')

    model_dir = os.path.join(args.model_dir, 'model.joblib')
    joblib.dump(model, model_dir)
    print(f'Model saved to: {model_dir}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_estimators', type=int, default=100)
    parser.add_argument('--max_depth', type=int, default=10)
    parser.add_argument('--random_state', type=int, default=42)
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN', '.'))
    parser.add_argument('--model_dir', type=str, default=os.environ.get('SM_MODEL_DIR', '../models'))

    args = parser.parse_args()
    train(args)
