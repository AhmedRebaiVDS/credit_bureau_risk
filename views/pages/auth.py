
from dash import dcc, Input, Output, html, callback_context, callback,State
import requests
import os
layout= html.Div([
    html.Div(id="hidden_div_for_redirect_callback"),

    html.Div([

        html.Img(src="assets/Value.jpg")

    ],className="logo"),
    
    html.Div("Login Form",className="text-center mt-4 name"),
    html.Div([
        
        html.Div([
            html.Span(className="far fa-user"),
            dcc.Input(placeholder="Email",id="email",required=True,type="email")
        ],className='form-field d-flex align-items-center'),
        html.Div([
             html.Span(className="fas fa-key"),
            dcc.Input(placeholder="Password",id="password",required=True,type="password")
        ],className='form-field d-flex align-items-center'),
        html.Div([
           html.Button("Log In",id="SubmitLogin",className="btn mt-3",type="submit" ,n_clicks=0),
           
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
              
              Input('SubmitLogin', 'n_clicks'),
              State('email', 'value'),
              State('password', 'value'),
              )
def update_output(btn,email,password):

    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    print(os.environ)
    
    if (btn>0 and email and password and "SubmitLogin" in changed_id ):
            r=requests.post("https://bank-risk-dashboard.herokuapp.com/user/login",json={"email":email,"password":password})
            if r.status_code==200:
                return r.json()["token"],dcc.Location(pathname="/home", id="someid_doesnt_matter")
            return [],""
    return [],""