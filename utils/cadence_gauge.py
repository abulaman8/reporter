import plotly.graph_objects as go
import base64


def cad_plot(value=114, ref=150):

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Cadence", 'font': {'size': 16}},
        delta={'reference': ref, 'increasing': {
            'color': 'green'}, 'decreasing': {'color': 'red'}},
        gauge={
            'axis': {'range': [120, 210], 'tickwidth': 1, 'tickcolor': "darkblue", 'tickfont': {'size': 12}},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [120, 150], 'color': 'yellow'},
                {'range': [150, 180], 'color': 'orange'},
                {'range': [180, 210], 'color': 'red'}
            ],
        }
    ))
    fig.update_layout(
        width=458,
        height=337
    )

    img = fig.to_image(format="png")

    return base64.b64encode(img).decode()
