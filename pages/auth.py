from doctest import FAIL_FAST
from dash import dcc, Input, Output, html, callback_context, callback,State


layout= html.Div([
    html.Div(id="hidden_div_for_redirect_callback"),

    html.Div([

        html.Img(src="assets/Value.jpg")

    ],className="logo"),
    
    html.Div("Login Form",className="text-center mt-4 name"),
    html.Div([
        
        html.Div([
            html.Span(className="far fa-user"),
            dcc.Input(placeholder="Username",id="username",required=True,type="text")
        ],className='form-field d-flex align-items-center'),
        html.Div([
             html.Span(className="fas fa-key"),
            dcc.Input(placeholder="Password",id="password",required=True,type="password")
        ],className='form-field d-flex align-items-center'),
        html.Div([
            html.Button("log in ",id="submit",className="btn mt-3"),
           
        ],className="p-3 mt-3"),
        html.Div([
            html.A("Lost your password ",href="lost-password"),
            "or",
            html.A(" Register",href="lost-password"),

        ],className="text-center fs-6")
 
],className="p-3 mt-3")],className="wrapper")


@callback    (
              Output('localstorage', 'data'),
              Output('hidden_div_for_redirect_callback', 'children'),
              State('username', 'value'),
              State('password', 'value'),
              Input('submit', 'n_clicks'),
              )
def update_output(user,password,btn):

    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'submit' in changed_id:
        if(user=="root" and password=="root"):
            return True,dcc.Location(pathname="/home", id="someid_doesnt_matter")
        return [], ""
    return [],""