import plotly.graph_objects as go
import base64


def cad_plot(value=114, ref=100):

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Cadence", 'font': {'size': 24}},
        delta={'reference': ref, 'increasing': {
            'color': 'green'}, 'decreasing': {'color': 'red'}},
        gauge={
            'axis': {'range': [60, 150], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [60, 90], 'color': 'yellow'},
                {'range': [90, 125], 'color': 'orange'},
                {'range': [125, 150], 'color': 'red'}
            ],
        }
    ))

    img = fig.to_image(format="png")

    return base64.b64encode(img).decode()
