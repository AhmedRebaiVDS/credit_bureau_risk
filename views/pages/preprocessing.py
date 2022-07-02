
from dash import  html


import matplotlib
matplotlib.use('Agg')

from views.components import sidebar,preprocessing

CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(preprocessing.layout, className="content")

layout = html.Div([
    sidebar.sidebar,
    content
])
