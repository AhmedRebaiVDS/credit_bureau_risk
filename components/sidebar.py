
import dash_html_components as html




SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "backgroundColor": "#f8f9fa",
}


CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Welcome to your dashboard", className="lead"
        ),
        html.Nav(
            [
                html.A("Home", href="/home"),
                html.A("EDA", href="/eda"),
                html.A("Preprocessing", href="/preprocessing"),
            ],
           
        ),
    ],
    style=SIDEBAR_STYLE,
    
)

