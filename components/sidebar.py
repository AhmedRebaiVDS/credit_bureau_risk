
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import  callback, callback_context,dcc
from dash.dependencies import Input, Output, State

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
        html.Div(id="matter"),

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
                    href="/home",
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
        html.Button(
                    [
                        html.Span(className="fas fa-power-off me-2"),
                      
                    ],

                    id='logout',
                    className="btn-logout"
                )
    ],

    className="sidebar",
)
@callback(  Output('localstorage', 'clear_data'),Output('matter', 'children')

,
           Input('logout', 'n_clicks'))
def logout(btn):
    
    if btn:
        return True,dcc.Location(pathname="/",id="maatter")
    return False,''
  