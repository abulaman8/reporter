import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import joblib
import numpy as np
import pandas as pd

file = "student_data.csv"
student_data = pd.read_csv(file)

student_data = student_data[["Cadence(steps/min)", "Heart rate(bpm)"]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(student_data)


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

print(f"Optimal K: {optimal_k}")

kmeans = KMeans(n_clusters=optimal_k, random_state=8)
model = kmeans.fit(scaled_features)
joblib.dump(model, 'cad_bpm_cluster_model.pkl')

cluster_labels = model.predict(scaled_features)

student_data['Cluster'] = cluster_labels

cluster_names = {
    0: "Low Cadence, Low BPM",
    1: "High Cadence, Low BPM",
    2: "High Cadence, High BPM",
    3: "Low Cadence, High BPM"
}


def find_cluster(new_data_point, scaler, kmeans_model):
    new_data_scaled = scaler.transform([new_data_point])
    predicted_cluster = kmeans_model.predict(new_data_scaled)
    return predicted_cluster[0]


new_data_point = [114, 94]
predicted_cluster = find_cluster(new_data_point, scaler, kmeans)
print(
    f"Hassan belongs to cluster {predicted_cluster} ({cluster_names[predicted_cluster]}).")

plt.figure(figsize=(10, 6))

# Plot all points with some transparency
scatter = plt.scatter(
    student_data["Cadence(steps/min)"], student_data["Heart rate(bpm)"],
    c=student_data["Cluster"], cmap='viridis', s=50, alpha=0.7, edgecolor='k')

# Plot Hassan's data point with a border
plt.scatter(new_data_point[0], new_data_point[1],
            color='red', marker='*', s=300, edgecolor='black', linewidth=2, label='Hassan')

cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
# plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1],
#             color='black', marker='X', s=200, label='Cluster Centers')

plt.legend(loc='upper right')
plt.title(f'K-Means Clustering (K={optimal_k})')
plt.xlabel('Cadence (steps/min)')
plt.ylabel('Heart rate (bpm)')
plt.grid(True)
plt.show()

output_file_path = 'output.csv'
student_data.to_csv(output_file_path, index=False)
print(f"CSV file saved at {output_file_path}")
