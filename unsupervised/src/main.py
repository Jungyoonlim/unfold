from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from clean import df 

X = df[['BeginDate', 'EndDate']]

# Assuming you want to cluster based on 'BeginDate' and 'EndDate', modify as needed
X = df[['BeginDate', 'EndDate']]

# Standardizing the features based on standard scaler
sc = StandardScaler()
X = sc.fit_transform(X)

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters=3, random_state=42)

# Fit model to points
model.fit(X)

# Determine the cluster labels of X: labels
labels = model.predict(X)

# Print cluster labels of X
print(labels)