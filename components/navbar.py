
import dash_bootstrap_components as dbc



navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("sign-in", href="/sign-in")),
        dbc.NavItem(dbc.NavLink("sign-up", href="/sign-up")),
        dbc.NavItem(dbc.NavLink("home", href="/home")),
        
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)