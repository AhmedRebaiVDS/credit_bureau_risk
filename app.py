
import plotly.express as px  
from dash import Dash, dcc, Input, Output, html, callback_context, callback

from dash.dependencies import Input, Output, State

import base64
from pandas_profiling import ProfileReport
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

from pages import eda,preprocessing


app = Dash(__name__,suppress_callback_exceptions=True)
server=app.server



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
  
    html.Div(id='page-content')
])



@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/eda':
        return eda.layout
    elif pathname == '/preprocessing':
        return preprocessing.layout
    elif  pathname == '/':
        return html.Div([
               
                    dcc.Link('Navigate to eda', href='/eda'),
                    html.Br(),
                    dcc.Link('Navigate to preprocessing', href='/preprocessing'),
                   
                ])
    else: 
         return '404'

if __name__ == '__main__':
    app.run_server(debug=True)