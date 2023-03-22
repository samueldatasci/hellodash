import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

# Dataset Processing

path = 'https://raw.githubusercontent.com/nalpalhao/DV_Practival/master/datasets/'

df = pd.read_csv(path + 'emissions.csv')

# Requirements for the dash core components

country_options = [
    {'label': 'Country Portugal', 'value': 'Portugal'},
    {'label': 'Country Spain', 'value': 'Spain'},
    {'label': 'Country France', 'value': 'France'}
]
"""
Equivalent way to iteratively build country_options from the dataset's countries:

country_options = [
    dict(label='Country ' + country, value=country)
    for country in df['country_name'].unique()]
 
 Try it out!
"""

gas_options = [
    {'label': 'GHG Emissions', 'value': 'GHG_emissions'},
    {'label': 'F-Gas Emissions', 'value': 'F_Gas_emissions'},
    {'label': 'CO2 Emissions', 'value': 'CO2_emissions'}
]

# The app itself

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1('Countries Emissions'),

    dcc.Dropdown(
        id='country_drop',
        options=country_options,
        value=['Portugal'],
        multi=True
    ),

    html.Br(),

    dcc.RadioItems(
        id='gas_radio',
        options=gas_options,
        value='CO2_emissions'
    ),

    dcc.Graph(id='graph_example'),

    html.Br(),

    dcc.RangeSlider(
        id='year_slider',
        min=1990,
        max=2014,
        value=[1990, 2014],
        marks={'1990': 'Year 1990',
               '1995': 'Year 1995',
               '2000': 'Year 2000',
               '2005': 'Year 2005',
               '2010': 'Year 2010',
               '2014': 'Year 2014'},
        step=1
    )
])


@app.callback(
    Output('graph_example', 'figure'),
    [Input('country_drop', 'value'),
     Input('gas_radio', 'value'),
     Input('year_slider', 'value')]
)
def update_graph(countries, gas, year):
    filtered_by_year_df = df[(df['year'] >= year[0]) & (df['year'] <= year[1])]

    scatter_data = []

    for country in countries:
        filtered_by_year_and_country_df = filtered_by_year_df.loc[filtered_by_year_df['country_name'] == country]

        temp_data = dict(
            type='scatter',
            y=filtered_by_year_and_country_df[gas],
            x=filtered_by_year_and_country_df['year'],
            name=country
        )

        scatter_data.append(temp_data)

    scatter_layout = dict(xaxis=dict(title='Year'),
                          yaxis=dict(title=gas)
                          )

    fig = go.Figure(data=scatter_data, layout=scatter_layout)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
