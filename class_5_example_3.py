import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Dataset Processing

path = 'https://raw.githubusercontent.com/nalpalhao/DV_Practival/master/datasets/Lesson_1/'

df = pd.read_excel(path + 'hw_1_data.xlsx', sheet_name='ex3')
df = df.drop(6, errors='ignore')  # Drops the 'total sales' row

# Requirements for the dash core components

options = [{'label': 'Month of July', 'value': 'July'},
           {'label': 'Month of August', 'value': 'August'},
           {'label': 'Month of September', 'value': 'September'}]

# The App itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1('Exercise 3 Data Visualization Example'),

    html.Br(),

    html.Label('Choose a Month:'),
    dcc.Dropdown(
        id='drop',
        options=options,
        value='July'
    ),

    dcc.Graph(
        id='example-graph'
    )

])


@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id='drop', component_property='value')]
)
def callback_1(input_value):
    data_bar = dict(type='bar',
                    y=df[input_value],
                    x=df['Product'],
                    texttemplate='<b>%{y} €</b>',
                    textposition='outside'
                    )

    layout_bar = dict(yaxis=dict(range=(0, 1500),
                                 title='Monetary Units'
                                 )
                      )

    return go.Figure(data=data_bar, layout=layout_bar)


if __name__ == '__main__':
    app.run_server(debug=True)
