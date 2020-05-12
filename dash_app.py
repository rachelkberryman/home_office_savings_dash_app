#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 16:08:04 2020

@author: paulmora
"""

# %% 00 Packages and directories

# =============================================================================
# 00.0 Official python packages
# =============================================================================
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pickle
import numpy
from _classes import RentCalculator
from _config import city_price_dict, space_dict

# %% 01 Importing data

# City price dictionary
cities = city_price_dict
available_cities = sorted(cities.keys())
# Space requirement list
space_types = space_dict
available_types = sorted(space_types.keys())
# Days working from home
wfh_options = list(range(0, 5 + 1))
# Import
data_germany = pickle.load(open('assets' + "//data_germany.p", "rb"))
layout_germany = pickle.load(open('assets' + "//data_layout.p", "rb"))

# %% 01 Dashing

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {
    'background': '#001308',
    'text': '#DEE5E5'
}

# Initial figure for the rent calculation
figure = go.Figure(data=go.Bar(x=['Savings'], y=[0]),
                   layout=go.Layout(plot_bgcolor=colors['background'],
                                    paper_bgcolor=colors['background'],
                                    font={
                                        'color': colors['text']},
                                    xaxis=dict(
                                        showticklabels=False,
                                        autorange=True,
                                        showgrid=False
                                        ),
                                    yaxis=dict(
                                        showticklabels=False,
                                        autorange=True,
                                        showgrid=False
                                        ),
                                    ))

fig = go.Figure(data=data_germany,
                layout=layout_germany)

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[

    html.Div([
        html.Div([
            html.H5('Calculating Rent and potential savings',
                    style={
                        'color': colors['text'],
                        'margin-left': '2%'}),
            # Dropdown menu for all cities
            html.Div([
                html.Label('City Selection',
                           style={
                               'textAlign': 'center',
                               'color': colors['text']}),
                dcc.Dropdown(
                    id='city',
                    options=[{'label': i, 'value': i} for i in available_cities],
                    placeholder='Select a city')
                ], style={'width': '25%', 'display': 'inline-block',
                          'verticalAlign': 'middle',
                          'margin-left':'2%'}),
            # Input for all employees
            html.Div([
                html.Label('Employee amount',
                           style={
                            'textAlign': 'center',
                            'color': colors['text']}),
                dcc.Input(
                    id='employees',
                    placeholder='# Employees', type='text',
                    size='12'),
                ], style={'width': '25%', 'display': 'inline-block',
                          'verticalAlign': 'middle',
                          'margin-left':'2%'}),
            # Dropdown menu for the space requirements in the office
            html.Div([
                html.Label('Space Selection',
                           style={
                            'textAlign': 'center',
                            'color': colors['text']}),
                dcc.Dropdown(
                    id='space',
                    options=[{'label': i, 'value': i} for i in available_types],
                    placeholder='Select a space type')
                ], style={'width': '25%', 'display': 'inline-block',
                          'verticalAlign': 'middle',
                          'margin-left':'2%'}),
            html.Div([
                dcc.Graph(id='saving_graph', figure=figure)
            ]),
            html.Div([
                dcc.Slider(
                        id='wfh_days',
                        min=min(wfh_options),
                        max=max(wfh_options),
                        value=min(wfh_options),
                        marks={str(day): str(day) for day in wfh_options},
                        step=None)
            ], style={'width': '100%', 'display': 'inline-block',
                      'padding': '0 20'}),
        ], className="six columns"),

        html.Div([
            html.H5('Checking square meter price by city',
                    style={
                        'textAlign': 'left',
                        'color': colors['text']}),
            dcc.Graph(figure=fig)
        ], className="six columns"),
    ], className="row")
])




@app.callback(
    Output(component_id='saving_graph', component_property='figure'),
    [Input(component_id='city', component_property='value'),
     Input(component_id='employees', component_property='value'),
     Input(component_id='space', component_property='value'),
     Input(component_id='wfh_days', component_property='value'),
     ])


def update_value(city, employees, space, wfh_days):
    rent = RentCalculator(str(city),
                          float(employees),
                          str(space),
                          float(wfh_days))

    return {
        'data' : [
                go.Bar(
                    x=['Savings'],
                    y=[rent.rent - rent.savings],
                    name='Rent',
                    marker = dict(color='#149414')
                    ),
                go.Bar(
                    x=['Savings'],
                    y=[rent.savings],
                    name='Savings',
                    marker = dict(color='white')
                    )
                ],
        'layout':
                go.Layout(barmode='stack',
                          plot_bgcolor = colors['background'],
                          paper_bgcolor= colors['background'],
                          font = {'color': colors['text']})
    }

if __name__ == '__main__':
    app.run_server(debug=False)
