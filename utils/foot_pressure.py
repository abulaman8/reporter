import plotly.graph_objects as go
import base64


def pressure_plot(lt=32, lh=25, rt=28, rh=25):
    leg_labels = ['Left Toe', 'Left Heel', 'Right Toe', 'Right Heel']
    recorded_values = [lt, lh, rt, rh]
    # recorded_values = [32, 25, 28, 25]

    low_range_end = 20
    normal_range_end = 40
    high_range_end = 60

    fig = go.Figure()

    for i, label in enumerate(leg_labels):

        fig.add_trace(go.Bar(
            x=[label],
            y=[low_range_end],
            base=[0],
            name='Low range (0 to 20 kPa)',
            marker_color='pink',
            hoverinfo='none',
            width=0.6
        ))

        fig.add_trace(go.Bar(
            x=[label],
            y=[normal_range_end - low_range_end],
            base=[low_range_end],
            name='Normal range (20 to 40 kPa)',
            marker_color='turquoise',
            hoverinfo='none',
            width=0.6
        ))

        fig.add_trace(go.Bar(
            x=[label],
            y=[high_range_end - normal_range_end],
            base=[normal_range_end],
            name='High range (40 to 60 kPa)',
            marker_color='pink',
            hoverinfo='none',
            width=0.6,
            # set font size 20
        ))

    for i, value in enumerate(recorded_values):
        fig.add_trace(go.Bar(
            x=[leg_labels[i]],
            y=[value],
            base=[0],
            width=0.2,
            marker_color='blue',
            name=f'Recorded value {value} kPa',
            hoverinfo='none'
        ))

        fig.add_trace(go.Scatter(
            x=[leg_labels[i]],
            y=[value],
            mode='text',
            text=[f'{value} kPa'],
            textposition='top center',
            showlegend=False,
            textfont=dict(color='blue', size=18),
        ))

    fig.update_layout(
        title="Leg Pressure Distribution (Toe and Heel)",
        xaxis_title="Leg Position",
        yaxis_title="Pressure (kPa)",
        yaxis=dict(range=[0, 60]),
        barmode='overlay',
        showlegend=False,
        xaxis_title_font=dict(size=20),
        yaxis_title_font=dict(size=20),
        xaxis_tickfont=dict(size=20),
        yaxis_tickfont=dict(size=20),
        title_font=dict(size=28)
    )

    img = fig.to_image(format="png")
    return base64.b64encode(img).decode()
