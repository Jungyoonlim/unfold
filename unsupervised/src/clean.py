import pandas as pd

# URL of the CSV file
url = 'https://github.com/Jungyoonlim/collection/blob/master/Artists.csv?raw=true'

# Use pandas to load the CSV file
df = pd.read_csv(url)

# Check the first few rows of the DataFrame
print(df.head())

# Check the number of missing values in each column
print(df.isnull().sum())

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode().iloc[0])
    else:
        df[col] = df[col].fillna(df[col].median())

print(df.isnull().sum())
