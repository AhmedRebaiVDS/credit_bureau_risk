
import dash_html_components as html
import dash_bootstrap_components as dbc



SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
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
        html.Div(
            [
                # width: 3rem ensures the logo is the exact width of the
                # collapsed sidebar (accounting for padding)
                html.Img(src="./assets/Value.jpg", style={"width": "3rem"}),
                html.H2("Dashboard"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Home")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-chart-bar me-2"),
                        html.Span("EDA"),
                    ],
                    href="/eda",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-brain me-2"),
                        html.Span("Preprocessing"),
                    ],
                    href="/preprocessing",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)