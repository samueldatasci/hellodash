import dash
from dash import dcc
from dash import html
from datetime import datetime as dt


options = [{'label': 'Portugal', 'value': 'PT'},
           {'label': 'Spain', 'value': 'SP'},
           {'label': 'France', 'value': 'FR'}]

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Label('Dropdown'),
    dcc.Dropdown(
        id='drop',
        options=options,
        value='PT'
    ),

    html.Br(),
    html.Hr(),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        id='multidrop',
        options=options,
        value=['PT', 'FR'],
        multi=True
    ),

    html.Br(),
    html.Hr(),

    html.Label('Text Input'),
    dcc.Input(
        id='input',
        value='PT',
        type='text'),

    html.Br(),
    html.Hr(),

    html.Label('Slider'),
    dcc.Slider(
        id='slider',
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) for i in range(1, 6)},
        value=5,
        step=1
    ),

    html.Br(),
    html.Hr(),

    html.Label('Range Slider'),
    dcc.RangeSlider(
        id='rangeslider',
        marks={i: 'Label {}'.format(i) for i in range(0, 9)},
        min=0,
        max=9,
        value=[0, 1],
        step=1
    ),
    html.Br(),
    html.Hr(),

    html.Label('Text Area'),
    dcc.Textarea(
        id='textarea',
        placeholder='Enter a value...',
        value='This is a TextArea component'
    ),

    html.Br(),
    html.Hr(),

    html.Label('Date Picker Single'),
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt(2019, 6, 12)
    ),

    html.Br(),
    html.Hr(),

    html.Label('Radio Items'),
    dcc.RadioItems(
        id='radio',
        options=options,
        value='PT'
    ),

    html.Br(),
    html.Hr(),

    html.Label('Checkboxes'),
    dcc.Checklist(
        id='checkbox',
        options=options,
        value=['PT', 'FR']
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)