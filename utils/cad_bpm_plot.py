import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd
import io
import base64


def find_cluster(new_data_point, scaler, kmeans_model):
    new_data_scaled = scaler.transform([new_data_point])
    predicted_cluster = kmeans_model.predict(new_data_scaled)
    return predicted_cluster[0]


def cad_bpm_plot(cadence=114, heart_rate=94):
    """
    Plotting the Cadence vs. Heart Rate data
    :param cadence:
    :param heart_rate:
    :return:
    """
    file = "student_data.csv"
    student_data = pd.read_csv(file)

    student_data = student_data[["Cadence(steps/min)", "Heart rate(bpm)"]]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(student_data)

    model = joblib.load('cad_bpm_cluster_model.pkl')
    cluster_labels = model.predict(scaled_features)

    student_data['Cluster'] = cluster_labels

    cluster_names = {
        0: "Low Cadence, Low BPM",
        1: "High Cadence, Low BPM",
        2: "High Cadence, High BPM",
        3: "Low Cadence, High BPM"
    }

    new_data_point = [cadence, heart_rate]
    # new_data_point = [114, 94]
    predicted_cluster = find_cluster(new_data_point, scaler, model)

    plt.figure(figsize=(10, 6))

    scatter = plt.scatter(
        student_data["Cadence(steps/min)"], student_data["Heart rate(bpm)"],
        c=student_data["Cluster"], cmap='viridis', s=50, alpha=0.7, edgecolor='k')

    plt.scatter(new_data_point[0], new_data_point[1],
                color='red', marker='*', s=300, edgecolor='black', linewidth=2, label='Hassan')

    cluster_centers = scaler.inverse_transform(model.cluster_centers_)

    plt.legend(loc='upper right')
    plt.title(f'K-Means Clustering (K={model.n_clusters})')
    plt.xlabel('Cadence (steps/min)')
    plt.ylabel('Heart rate (bpm)')
    plt.grid(True)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return img
