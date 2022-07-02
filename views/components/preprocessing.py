

from dash import  dcc, Input, Output, html,  callback
from dash.dependencies import Input, Output, State
import base64
import io
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import dash_bootstrap_components as dbc

layout = html.Div([
    dcc.Upload(
        id='upload-data-merge',
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
       
        multiple=True
    ),
    html.Div(id='output-data-upload-file'),
    html.Div(id='select-column'),
    html.Button('Merge', id='btn-merge', n_clicks=0 ,style={
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
    html.Div(id='output-data-merge'),
    html.Button('Download', id='btn-download', n_clicks=0 ,style={
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
    dcc.Download(id="download-dataframe-csv"),
    html.Div(id='output-data-download'),
    dcc.Store(id="store-data",data=[],storage_type='memory'),
    dcc.Store(id="store-data-merged",data=[],storage_type='memory'),

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
    return df,filename


@callback(    Output('output-data-upload-file', 'children'),
              Output('store-data', 'data'),  
              Output('select-column', 'children'),  
              Input('upload-data-merge', 'contents'),
              State('upload-data-merge', 'filename'),
              State('upload-data-merge', 'last_modified'))
        
def store_data(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None :

        df1,n1=parse_contents(list_of_contents[0], list_of_names[0], list_of_dates[0])
        df2,n2=parse_contents(list_of_contents[1], list_of_names[1], list_of_dates[1])

        l1=df1.columns
        l2=df2.columns

        liste=[{"label":i,"value":i} for i in l1 for j in l2 if i==j]

        

        return n1+n2+" uploaded successfully",[df1.to_dict('records'),df2.to_dict('records')],dcc.Dropdown(
                                                                                        options=liste)
    return "",[],""



@callback(   
              Output('output-data-merge', 'children'),
              Output('store-data-merged', 'data'),  
              Input('store-data', 'data'),  
              Input('btn-merge', 'n_clicks'),
              Input('select-column', 'value'),
              
              prevent_initial_call=True,
)
def update_output(data,btn,value):

    if(btn>0):
        df1=pd.DataFrame(data[0])
        df2=pd.DataFrame(data[1])
        


        df1=df2.merge(df1,how="inner",on=value)

        return "Merged successfully",df1.to_dict('records')
    return "",[]
    

@callback(   
              Output('output-data-download', 'children'),
              Output('download-dataframe-csv', 'data'),
              Input('store-data-merged', 'data'),  
              Input('btn-download', 'n_clicks'),
              
              prevent_initial_call=True,
)
def update_output(data,btn):

    if(btn>0 and len(data)!=0):
        df=pd.DataFrame(data)
        return "Downloaded successfully",dcc.send_data_frame(df.to_csv, "mydf-merged.csv")

    return "",None   