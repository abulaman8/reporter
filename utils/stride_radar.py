import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import base64
import io


def stride_radar_plot(data=[0.7, 0.82, 0.35, 0.44]):
    # kid_data = [0.7, 0.82, 0.35, 0.44]
    kid_data = data

    # Average ranges for the age group (taking the average of the ranges)
    avg_data = [
        (0.5 + 1) / 2,     # stride length
        (0.8 + 1.2) / 2,   # stride velocity
        (0.3 + 0.5) / 2,   # swing time
        (0.5 + 1) / 2      # stance time
    ]

    # Parameters (axes labels)
    labels = ['Stride Length', 'Stride Velocity', 'Swing Time', 'Stance Time']

    # Number of variables we're plotting (must match the number of data points)
    num_vars = len(labels)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Make the plot circular by closing the loop
    kid_data += kid_data[:1]
    avg_data += avg_data[:1]
    angles += angles[:1]

    # Create the radar plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Set a vibrant color map for the plot
    colors = cm.get_cmap('coolwarm')

    # Plot the kid's data with more vibrant colors and adjust alpha transparency
    ax.fill(angles, kid_data, color=colors(0.2), alpha=0.5,
            linewidth=2, label='Kid\'s Performance')
    ax.plot(angles, kid_data, color=colors(
        0.2), linewidth=3, linestyle='solid')

    # Plot the average data with a contrasting color
    ax.fill(angles, avg_data, color=colors(0.8), alpha=0.4,
            linewidth=2, label='Average Performance')
    ax.plot(angles, avg_data, color=colors(
        0.8), linewidth=3, linestyle='dashed')

    # Add number tips for kid's performance inside the blue area
    for i, (angle, value) in enumerate(zip(angles, kid_data)):
        if i < len(kid_data) - 1:  # Avoid repeating the first point
            offset = -0.05  # Push numbers slightly inside the area
            ax.text(angle, value + offset,
                    f'{value:.2f}', size=10, color='blue', ha='center', va='bottom')

    # Add number tips for average performance outside the red area
    for i, (angle, value) in enumerate(zip(angles, avg_data)):
        if i < len(avg_data) - 1:  # Avoid repeating the first point
            offset = 0.05  # Push numbers slightly outside the area
            ax.text(angle, value + offset,
                    f'{value:.2f}', size=10, color='red', ha='center', va='top')

    # Add labels for each axis with custom styling
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=14, color='navy', weight='bold')

    # Customizing the radial axis grid
    ax.yaxis.grid(True, color='gray', linestyle='dotted', linewidth=1)
    ax.xaxis.grid(True, color='gray', linestyle='dotted', linewidth=1)

    # Add a title with some style
    ax.set_title('Kid\'s Sports Performance vs Average', size=18,
                 color='darkblue', pad=30, weight='bold')

    # Customizing radial ticks
    ax.set_yticklabels([])
    # Remove the outer circle for a cleaner look
    ax.spines['polar'].set_visible(False)

    # Add a fancy legend outside the plot
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1),
              fontsize=12, frameon=True, fancybox=True, shadow=True)

    # Show the plot
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return img
