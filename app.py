from dash import Dash, dcc, Input, Output, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import matplotlib
matplotlib.use('Agg')
from pages import eda,preprocessing,home
import dash_auth

users=[['root','root']]

app = Dash(__name__,suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server

auth=dash_auth.BasicAuth(app,users)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif  pathname == '/home':
        return home.layout
    elif  pathname == '/eda':
        return eda.layout
    elif  pathname == '/preprocessing':
        return preprocessing.layout

if __name__ == '__main__':
    app.run_server(debug=True)