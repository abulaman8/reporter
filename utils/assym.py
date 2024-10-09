import plotly.graph_objects as go
import base64


def assym_plot(data=[5, 5, 8, 4]):

    categories = ['Stride length asymmetry', 'Stride velocity asymmetry',
                  'Swing time asymmetry', 'Stance time asymmetry']
    hassan_asymmetry = [abs(v) for v in data]
    p_of_asymmetry = [1, 2, 1, 1]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=categories,
        y=hassan_asymmetry,
        name="Subject's data",
        marker_color='#2E105E',
        yaxis='y1',
        width=0.4,
        text=[f'{v:.2f}%' for v in hassan_asymmetry],
        textposition='auto',
        textfont=dict(size=16),
        offsetgroup=0
    ))

    fig.add_trace(go.Bar(
        x=categories,
        y=p_of_asymmetry,
        name="% of Runners with assymmetry",
        marker_color='#F9A7A5',
        yaxis='y2',
        width=0.4,
        text=[f'{v:.2f}%' for v in p_of_asymmetry],
        textposition='auto',
        textfont=dict(size=16),
        offsetgroup=1
    ))

    fig.update_layout(
        title="Subject's Asymmetry vs % of Runners with Asymmetry",
        xaxis=dict(
            title="Asymmetry Parameters"
        ),
        yaxis=dict(
            title="Subject's Asymmetry %",
            range=[0, 10],
            titlefont=dict(color='#2E105E'),
            tickfont=dict(color='#2E105E')
        ),
        yaxis2=dict(
            title="% of Runners with Asymmetry",
            range=[0, 3],
            overlaying='y',
            side='right',
            titlefont=dict(color='#F9A7A5'),
            tickfont=dict(color='#F9A7A5')
        ),
        legend=dict(x=0.5, y=-0.15, orientation="h",
                    xanchor="center", yanchor="top"),
        xaxis_title_font=dict(size=20),
        yaxis_title_font=dict(size=20),
        yaxis2_title_font=dict(size=20),
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=20),
        title_font=dict(size=28)
    )

    img = fig.to_image(format="png")

    return base64.b64encode(img).decode('utf-8')
