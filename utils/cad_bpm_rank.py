import pandas as pd
from scipy import stats


def cad_bpm_rank(cadence=114, heart_rate=94):
    file = "student_data.csv"
    student_data = pd.read_csv(file)

    # Extract relevant columns
    student_data = student_data[["Cadence(steps/min)", "Heart rate(bpm)"]]

    # Hassan's data point
    hassan_data_point = [cadence, heart_rate]
    # hassan_data_point = [114, 94]

    # Calculate percentile ranks for each feature
    percentile_ranks = {
        "Cadence(steps/min)": stats.percentileofscore(student_data["Cadence(steps/min)"], hassan_data_point[0], kind='rank'),
        "Heart rate(bpm)": stats.percentileofscore(student_data["Heart rate(bpm)"], hassan_data_point[1], kind='rank')
    }

    # print(f"Hassan's Percentile Ranks:")
    # print(f"Cadence(steps/min): {percentile_ranks['Cadence(steps/min)']}%")
    # print(f"Heart rate(bpm): {percentile_ranks['Heart rate(bpm)']}%")

    # Calculate combined percentile standing (average of the two percentiles)
    combined_percentile = (
        percentile_ranks['Cadence(steps/min)'] + percentile_ranks['Heart rate(bpm)']) / 2
    # print(f"Combined Percentile Standing: {combined_percentile}%")
    return combined_percentile
