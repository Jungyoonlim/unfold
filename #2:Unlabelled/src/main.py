from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from clean import clean_data

# Get the clean data
df = clean_data()

X = df[['BeginDate', 'EndDate']]

# Standardizing the features based on standard scaler
sc = StandardScaler()
X = sc.fit_transform(X)

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters=3, n_init=10, random_state=42)

# Fit model to points
model.fit(X)

# Determine the cluster labels of X: labels
labels = model.predict(X)

df['Cluster'] = labels

for i in range(3):
    print(f"cluster {i}:")
    print(df[df['Cluster'] == i].head())
    print("\n")