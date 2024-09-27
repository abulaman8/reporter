import plotly.graph_objects as go
import base64


def cop_plot(recorded_values=[1, -0.3]):
    leg_labels = ['Left', 'Right']
    # recorded_values = [1, -0.3]

    low_range_end = -2
    middle_range_end = 2
    high_range_end = 4

    fig = go.Figure()

    for i, label in enumerate(leg_labels):

        fig.add_trace(go.Bar(
            x=[label],
            y=[abs(-2 - (-4))],
            base=[-4],
            name=f'Low range (-4 to -2 cm)',
            marker_color='pink',
            hoverinfo='none',
            width=0.4
        ))

        fig.add_trace(go.Bar(
            x=[label],
            y=[middle_range_end - low_range_end],
            base=[low_range_end],
            name=f'Middle range (-2 to 2 cm)',
            marker_color='turquoise',
            hoverinfo='none',
            width=0.4
        ))

        fig.add_trace(go.Bar(
            x=[label],
            y=[high_range_end - middle_range_end],
            base=[middle_range_end],
            name=f'High range (2 to 4 cm)',
            marker_color='pink',
            hoverinfo='none',
            width=0.4
        ))

    for i, value in enumerate(recorded_values):
        fig.add_trace(go.Bar(
            x=[leg_labels[i]],
            y=[value],
            base=[0],
            width=0.1,
            marker_color='blue',
            name=f'Recorded COP {value} cm',
            hoverinfo='none'
        ))

        fig.add_trace(go.Scatter(
            x=[leg_labels[i]],
            y=[value],
            mode='text',
            text=[f'{value} cm'],
            textposition='top center' if value > 0 else 'bottom center',
            showlegend=False,
            textfont=dict(color='blue', size=18),
            cliponaxis=False
        ))

    fig.update_layout(
        title="Center of Pressure (COP) Distribution",
        xaxis_title="Leg",
        yaxis_title="COP (cm from center)",
        yaxis=dict(range=[-4, 4], zeroline=True,
                   zerolinewidth=2, zerolinecolor='black'),
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
