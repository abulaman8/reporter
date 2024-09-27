import seaborn as sns
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd


file = "student_data.csv"
student_data = pd.read_csv(file)

student_data = student_data[["Cadence(steps/min)", "Heart rate(bpm)"]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(student_data)
# scaled_features = scaler.fit_transform(features)


def optimal_k_means(data, max_clusters=10):
    silhouette_scores = []
    k_values = range(2, max_clusters+1)

    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=8)
        cluster_labels = kmeans.fit_predict(data)
        silhouette_avg = silhouette_score(data, cluster_labels)
        silhouette_scores.append(silhouette_avg)

    optimal_k = k_values[np.argmax(silhouette_scores)]
    return optimal_k, silhouette_scores


optimal_k, silhouette_scores = optimal_k_means(scaled_features)

print(f"optimal K: {optimal_k}")

kmeans = KMeans(n_clusters=optimal_k, random_state=8)
cluster_labels = kmeans.fit_predict(scaled_features)
#
# # Reduce dimensionality to 2D using PCA for visualization
# pca = PCA(n_components=2)
# pca_components = pca.fit_transform(scaled_features)
#
# # Plotting the clusters
# plt.figure(figsize=(10, 6))
# scatter = plt.scatter(
#     pca_components[:, 0], pca_components[:, 1], c=cluster_labels, cmap='viridis', s=50)
# plt.colorbar(scatter)
# plt.title('K-Means Clustering (K=9) with PCA Projection')
# plt.xlabel('Principal Component 1')
# plt.ylabel('Principal Component 2')
# plt.grid(True)
# plt.show()
student_data['Cluster'] = cluster_labels
output_file_path = 'output.csv'

# Save the updated dataframe to a CSV file
student_data.to_csv(output_file_path, index=False)

print(f"CSV file saved at {output_file_path}")
cluster_stats = {}

grouped = student_data.groupby('Cluster')
for name, group in grouped:
    cluster_stats[name] = group.describe().T

for cluster, stats in cluster_stats.items():
    print(f"Cluster {cluster}:\n")
    print(stats)
    print("-----------------------------"*5)
