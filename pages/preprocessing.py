
from dash import  html


import matplotlib
matplotlib.use('Agg')

from components import sidebar,preprocessing

CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(preprocessing.layout, style=CONTENT_STYLE)

layout = html.Div([
    sidebar.sidebar,
    content
])
