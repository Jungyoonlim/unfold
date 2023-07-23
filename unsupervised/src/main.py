import pandas as pd
import json

with open('collection.json', 'r') as f:
    data = json.load(f)

df = pd.json_normalize(data["data"])
print(df.head())
