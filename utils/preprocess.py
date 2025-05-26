import pandas as pd

def preprocess_data(df):
    # Exemple de prétraitement simple
    df = df.copy()
    df = df.dropna()
    if 'FTR' in df.columns:
        df = df.drop(columns=['FTR'])
    return df