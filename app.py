import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
from matrix import Matrix

import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Schelling Racial Segregation'),

    html.Div(children='''
        Schelling Racial Segregation - Simulation done by using Dash by Plotly.
    '''),

    dcc.Graph(id='matrix'),

    html.Div(children=[
        html.H2("Parameters"),
        html.Div(children=[
            html.P('Dimension (If you put 50 it will be 50x50):'),
            dcc.Input(
                id='dimension',
                type='number',
                value=50
        )]),
        html.Div(children=[
            html.P('Empty Space:'),
            dcc.Slider(
                id='empty',
                min=0,
                max=1,
                value=0.3,
                step=0.1,
                marks={round(i, 1): round(i, 1) for i in np.linspace(0,1,11)} # Various hacks here
        )]),

        html.Div(children=[
            html.P('Red/Blue Ratio:'),
            dcc.Slider(
                id='ratio',
                min=0,
                max=1,
                value=0.5,
                step=0.1,
                marks={
                    round(i, 1): str(round(i, 1)) + "/" + str(round(1 - i, 1)) for i in np.linspace(0,1,11)
                } # More hacks here
        )]),

        html.Div(children=[
            html.P('Threshold:'),
            dcc.Slider(
                id='threshold',
                min=0,
                max=1,
                value=0.3,
                step=0.1,
                marks={round(i, 1): round(i, 1) for i in np.linspace(0,1,11)} # Various hacks here
        )]),
    ])
    
])

@app.callback(
    Output('matrix', 'figure'),
    [Input('dimension', 'value'),
     Input('empty', 'value'),
     Input('ratio', 'value'),
     Input('threshold', 'value')])

def update_matrix(dimension, empty, ratio, threshold):
    occupied_space = 1 - empty
    p_one = ratio * occupied_space
    p_two = (1 - ratio) * occupied_space
    matrix = Matrix(dimension, p_one, p_two, threshold)
    return {
        'data': [go.Heatmap(
            z=matrix.matrix, 
            showscale=False,
            colorscale=[[0, 'rgb(220,220,220)'], [0.5, 'rgb(255,0,0)'], [1, 'rgb(0,0,255)']]
        )],

        'layout': go.Layout(
            xaxis=dict(
                autorange=True,
                showgrid=False,
                zeroline=False,
                showline=False,
                ticks='',
                showticklabels=False
            ),
            yaxis=dict(
                autorange=True,
                showgrid=False,
                zeroline=False,
                showline=False,
                ticks='',
                showticklabels=False
            )
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)