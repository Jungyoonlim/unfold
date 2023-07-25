import pandas as pd

def clean_data():
    url = 'https://github.com/Jungyoonlim/collection/blob/master/Artists.csv?raw=true'
    df = pd.read_csv(url)
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna(df[col].mode().iloc[0])
        else:
            df[col] = df[col].fillna(df[col].median())
    return df 

