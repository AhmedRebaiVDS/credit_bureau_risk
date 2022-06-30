from dash import Dash, dcc, Input, Output, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State
import matplotlib
matplotlib.use('Agg')
from pages import eda,preprocessing,home,auth,dashboard
import dash_auth

# users=[['root','root']]

app = Dash(__name__,suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])
server=app.server

# auth=dash_auth.BasicAuth(app,users)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Store(id="localstorage",data=[],storage_type='local'),

])


@callback(Output('page-content', 'children'),
           Input('url', 'pathname'),
            Input('localstorage', 'data'),)
def display_page(pathname,local):
    if local ==[]:
        if pathname == '/':
            return home.layout
        elif  pathname == '/sign-in':
            return auth.layout
        return  "404"
    else :     
        if  pathname == '/home':
            return dashboard.layout
        elif  pathname == '/eda':
            return eda.layout
        elif  pathname == '/preprocessing':
            return preprocessing.layout

        return  "404"
      

if __name__ == '__main__':
    app.run_server(debug=True)