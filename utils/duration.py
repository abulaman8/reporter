import plotly.graph_objects as go


def create_activity_pie_chart():
    # Define the activities and their durations
    activities = ["Sprinting", "High Knees", "Long Jump"]
    durations = [15, 30, 60]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(
        labels=activities,
        values=durations,
        hole=0.3,  # Adjust this for a donut shape; use 0 for a full pie chart
        textinfo='label+percent',
        insidetextorientation='radial'
    )])

    # Customize layout
    fig.update_layout(
        title="Activity Duration Breakdown",
        annotations=[dict(text='Activities', x=0.5, y=0.5,
                          font_size=20, showarrow=False)]
    )

    # Show the chart
    fig.show()


# Call the function to display the chart
create_activity_pie_chart()
