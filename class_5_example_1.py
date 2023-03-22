import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Dataset Processing

x = np.array([1, 2, 3, 4, 5])
y = x * 2

# Building our Graphs

data_scatter = dict(type='scatter',
                    x=x,
                    y=y,
                    name='example'
                    )

layout_scatter = dict(xaxis=dict(title='X axis'),
                      yaxis=dict(title='Y axis')
                      )

fig_scatter = go.Figure(data=data_scatter, layout=layout_scatter)

# The App itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1('My First DashBoard'),

    html.Div('Example of html Container'),

    dcc.Graph(
        id='example-graph',
        figure=fig_scatter
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
