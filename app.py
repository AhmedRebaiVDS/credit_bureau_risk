
from dash import Dash, dcc, Input, Output, html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State
import matplotlib
matplotlib.use('Agg')
from views.pages import eda,preprocessing,home,auth,dashboard
from flask_mongoengine import MongoEngine
from flask import Flask


# users=[['root','root']]

server=Flask(__name__)

server.config['MONGODB_SETTINGS'] = {
	'db': 'stage',
    'host': 'mongodb+srv://first:first@cluster.6keue.mongodb.net/stage?retryWrites=true&w=majority'
}

db = MongoEngine(server)



app = Dash(__name__,server=server,suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME,"assets/style.css"])

from controllers.auth import user_api
app.server.register_blueprint(user_api, url_prefix='/user')
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
            return auth.layout
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



@app.server.route('/test')
def test():
    return 'e'

if __name__ == '__main__':
    app.server.run(debug=True,threaded=True,port=5000)