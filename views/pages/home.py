
from views.components import navbar
from dash import Dash, dcc, Input, Output, html, callback

import matplotlib
matplotlib.use('Agg')

CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

content = html.Img(src="assets/background.jpg",  style={'zIndex': 0,

                                                        'backgroundSize': "cover",
                                                        'height': "100vh",
                                                        'color': "#f5f5f5",
                                                        'justifyContent': "center",
                                                        'backgroundAttachment': "fixed",
                                                        'backgroundPosition': "center",
                                                        'position': "relative",
                                                        'right': 0,
                                                        'left': 0,
                                                        'textAlign': "center"})

layout = html.Div([
    navbar.layout,
    content
])
