
import dash_bootstrap_components as dbc



layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("sign-in", href="/sign-in")),
        dbc.NavItem(dbc.NavLink("sign-up", href="/sign-up")),
        
    ],
    brand="Navbar",
    brand_href="#",
    color="primary",
    dark=True,
)