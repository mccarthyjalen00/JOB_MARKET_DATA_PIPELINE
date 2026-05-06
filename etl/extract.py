import pandas as pd

def extract():

    df = pd.read_csv("data/jobs.csv")

    print(f"Extracted {len(df)} records")

    return df