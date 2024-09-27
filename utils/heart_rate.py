import plotly.graph_objects as go
import base64


def plot_heart_rate(person_min=[65, 70, 72], person_avg=[94, 95, 110], person_max=[133, 150, 107]):
    activities = ['Walking', 'Running', 'Jumping']

    low_start = [60, 60, 60]
    low_end = [75, 75, 75]

    normal_start = [75, 75, 75]
    normal_end = [110, 110, 110]

    high_start = [110, 110, 110]
    high_end = [180, 180, 180]

    # person_min = [65, 70, 72]
    # person_avg = [94, 95, 110]
    # person_max = [133, 150, 107]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=[low_end[i] - low_start[i]
            for i in range(len(activities))],  # Bar width for low
        y=activities,
        base=low_start,  # Starting position
        orientation='h',
        marker=dict(color='#000080'),  # Navy color
        name='Min bpm (> 60 bpm)'
    ))

    fig.add_trace(go.Bar(
        x=[normal_end[i] - normal_start[i]
            for i in range(len(activities))],  # Bar width for normal
        y=activities,
        base=normal_start,  # Starting position
        orientation='h',
        marker=dict(color='green'),
        name='Avg. bpm (75 to 110 bpm)'
    ))

    fig.add_trace(go.Bar(
        x=[high_end[i] - high_start[i]
            for i in range(len(activities))],  # Bar width for high
        y=activities,
        base=high_start,  # Starting position
        orientation='h',
        marker=dict(color='purple'),
        name='Max bpm (< 180 bpm)'
    ))

    fig.add_trace(go.Scatter(
        x=person_min,
        y=activities,
        mode='markers+text',  # Add text mode
        marker=dict(color='red', size=10, symbol='x'),
        text=person_min,  # Annotating with min bpm values
        textposition='top center',
        textfont=dict(color='white', size=10),
        name="Person's Min bpm"
    ))

    fig.add_trace(go.Scatter(
        x=person_avg,
        y=activities,
        mode='markers+text',  # Add text mode
        marker=dict(color='orange', size=10, symbol='circle'),
        text=person_avg,  # Annotating with avg bpm values
        textposition='top center',  # Position text above markers
        textfont=dict(color='white', size=10),
        name="Person's Avg bpm"
    ))

    fig.add_trace(go.Scatter(
        x=person_max,
        y=activities,
        mode='markers+text',  # Add text mode
        marker=dict(color='blue', size=10, symbol='diamond'),
        text=person_max,  # Annotating with max bpm values
        textposition='top center',  # Position text above markers
        textfont=dict(color='white', size=10),
        name="Person's Max bpm"
    ))

    fig.update_layout(
        title="Heart Rate Ranges with Person's Recorded Heart Rates",
        xaxis_title="Heart Rate (BPM)",
        yaxis_title="Activities",
        barmode='overlay',
        showlegend=True
    )

    img = fig.to_image(format="png")
    return base64.b64encode(img).decode()
