
import plotly.express as px  
from dash import Dash, dcc, Input, Output, html, callback_context
import plotly.graph_objects as go
import dask.dataframe as dd
from dash.dependencies import Input, Output, State
from os import listdir
from os.path import isfile, join
import base64
from pandas_profiling import ProfileReport
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

list_reports=[{"label":f.split(".")[0] ,"value":f.split(".")[0]} for f in listdir("./notebooks/EDA/rapports") if isfile(join("./notebooks/EDA/rapports", f))]


app = Dash(__name__)
server=app.server

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'cursor':'pointer'
        },
       
        multiple=False
    ),

    html.Button('Submit', id='btn', n_clicks=0 ,style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'cursor':'pointer'
        }),

    html.Div(id='output-data-upload'),
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
        
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return filename,df

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'),
              Input('btn', 'n_clicks'))
def update_output(list_of_contents, list_of_names, list_of_dates,bnt):
    if list_of_contents is not None:
       
        a,b=parse_contents(list_of_contents, list_of_names, list_of_dates)
        changed_id = [p['prop_id'] for p in callback_context.triggered][0]
        print(changed_id)

        if("btn" in changed_id):

            profile = ProfileReport(b, title="{} Profiling Report".format(a.split(".")[0]))
            profile.to_file("./assets/rapports/{}.html".format(a.split(".")[0]))
           
            return        [ html.Iframe(
             src="assets/rapports/{}.html".format(a.split(".")[0]),
             style={"height": "1067px", "width": "100%",'border-style': 'none'})]   
      
        return a
    return ""

if __name__ == '__main__':
    app.run_server(debug=True)