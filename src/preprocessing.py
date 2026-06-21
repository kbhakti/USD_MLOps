import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import joblib


def preprocess_data(input_path, output_dir):
    df_mat = pd.read_csv(os.path.join(input_path, 'student-mat.csv'), sep=';')
    df_por = pd.read_csv(os.path.join(input_path, 'student-por.csv'), sep=';')

    df_mat['subject'] = 'Math'
    df_por['subject'] = 'Portuguese'
    df = pd.concat([df_mat, df_por], axis=0, ignore_index=True)

    df['performance'] = (df['G3'] >= 12).astype(int)
    df = df.drop(columns=['G1', 'G2', 'G3'])

    binary_map = {
        'school': {'GP': 0, 'MS': 1}, 'sex': {'F': 0, 'M': 1},
        'address': {'U': 0, 'R': 1}, 'famsize': {'LE3': 0, 'GT3': 1},
        'Pstatus': {'T': 0, 'A': 1}, 'schoolsup': {'no': 0, 'yes': 1},
        'famsup': {'no': 0, 'yes': 1}, 'paid': {'no': 0, 'yes': 1},
        'activities': {'no': 0, 'yes': 1}, 'nursery': {'no': 0, 'yes': 1},
        'higher': {'no': 0, 'yes': 1}, 'internet': {'no': 0, 'yes': 1},
        'romantic': {'no': 0, 'yes': 1}
    }
    for col, mapping in binary_map.items():
        df[col] = df[col].map(mapping)

    multi_cat_cols = ['Mjob', 'Fjob', 'reason', 'guardian', 'subject']
    df = pd.get_dummies(df, columns=multi_cat_cols, drop_first=True, dtype=int)

    num_cols = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures',
                'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'student_processed.csv'), index=False)
    joblib.dump(scaler, os.path.join(output_dir, 'scaler.joblib'))

    return df


if __name__ == '__main__':
    input_path = '/opt/ml/processing/input'
    output_dir = '/opt/ml/processing/output'
    df = preprocess_data(input_path, output_dir)
    print(f'Preprocessing complete. Shape: {df.shape}')
