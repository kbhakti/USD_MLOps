import joblib
import os
import numpy as np


def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, 'model.joblib'))
    return model


def predict_fn(input_data, model):
    predictions = model.predict(input_data)
    return predictions
