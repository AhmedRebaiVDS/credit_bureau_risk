
import dash_html_components as html

from components import sidebar




CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}



content = html.Div(id="page-content-side-bar", children=[], style=CONTENT_STYLE)

layout = html.Div([
    sidebar.sidebar,
    content
])


    