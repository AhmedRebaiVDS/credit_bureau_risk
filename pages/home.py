
from dash import Dash, dcc, Input, Output, html, callback

import matplotlib
matplotlib.use('Agg')
from components import navbar

CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div("",  className="content")

layout = html.Div([
    navbar.layout,
    content
])