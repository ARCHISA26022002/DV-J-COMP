import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

acci=pd.read_csv("C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Accidents0514.csv")
cf=pd.read_csv("C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Casualties0514.csv")
vf=pd.read_csv("C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Vehicles0514.csv")

first_df=pd.merge(cf,acci,on='Accident_Index')
df=pd.merge(first_df,vf,on='Accident_Index')
df.isnull().sum()

df.drop('LSOA_of_Accident_Location',axis=1,inplace=True)
df.dropna(subset=['Location_Easting_OSGR','Location_Northing_OSGR', 'Longitude', 'Latitude'],axis=0,inplace=True)
df.dropna(subset=['Time'],axis=0,inplace=True)

df.isnull().values.any()

q8df= pd.DataFrame(data=df, columns=['Journey_Purpose_of_Driver','Sex_of_Driver','Age_of_Driver','Age_Band_of_Driver','Driver_Home_Area_Type'])
q8df=q8df[q8df.Sex_of_Driver !=-1]


#Heat Map 1
# def month(string):
#     return int(string[3:5])
# df['Month']=df['Date'].apply(lambda x: month(x))
# def hour(string):
#     s=string[0:2]
#     return int(s)
# df['Hour']=df['Time'].apply(lambda x: hour(x))
# q7df=pd.DataFrame(data=df,columns=['Hour','Day_of_Week','Month','Accident_Severity'])
# q7df=q7df[q7df.Accident_Severity ==1]

# def heatMap():
#     q7df=pd.DataFrame(data=df,columns=['Hour','Day_of_Week','Month','Accident_Severity'])
#     q7df=q7df[q7df.Accident_Severity ==1]
#     fig = px.imshow(q7df)
#     return fig

def BarPlot():
    fig = px.bar(q8df,x='Journey_Purpose_of_Driver',y='Age_of_Driver',color='Sex_of_Driver',labels={'Male','Female','Other'},title='Journey Purpose of Driver vs Age_of_Driver')
    return fig


#Muazz1
def number_of_accidents():
    acci=pd.read_csv('C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Accidents0514.csv')
    acci['Hour'] = acci['Time'].map(lambda x: str(x).split(':')[0])
    acci['Hour'] = acci['Hour'].apply(pd.to_numeric, errors='coerce')
    hour = []
    num_of_fatal_acci = []
    num_of_acci = []
    for i in range(24):
        hour.append(i)
        num_of_fatal_acci_hour = len(acci[(acci['Accident_Severity'] == 1) &(acci['Hour'] == i)])
        num_of_acci_hour = len(acci[acci['Hour'] == i])
        num_of_fatal_acci.append(num_of_fatal_acci_hour)
        num_of_acci.append(num_of_acci_hour)
        normalized_num_of_fatal_acci = list(np.array(num_of_fatal_acci) / np.array(num_of_acci) *100)
    fig = px.line(x=hour, y=num_of_fatal_acci, labels={'x':'Hour', 'y':'Total Number of Fatal Accidents'})
    return fig

#Muazz2
def number_of_accidents1():
    acci=pd.read_csv('C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Accidents0514.csv')
    acci['Hour'] = acci['Time'].map(lambda x: str(x).split(':')[0])
    acci['Hour'] = acci['Hour'].apply(pd.to_numeric, errors='coerce')
    hour = []
    num_of_fatal_acci = []
    num_of_acci = []
    for i in range(24):
        hour.append(i)
        num_of_fatal_acci_hour = len(acci[(acci['Accident_Severity']== 1) & (acci['Hour'] == i)])
        num_of_acci_hour = len(acci[acci['Hour'] == i])
        num_of_fatal_acci.append(num_of_fatal_acci_hour)
        num_of_acci.append(num_of_acci_hour)
        normalized_num_of_fatal_acci = list(np.array(num_of_fatal_acci) / np.array(num_of_acci) *100)
    fig = px.line(x=hour, y=num_of_acci, labels={'x':'Hour', 'y':'Total Number of Accidents'})
    return fig


#Muazz3
def number_of_accidents2():
    acci=pd.read_csv('C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Accidents0514.csv')
    acci['Hour'] = acci['Time'].map(lambda x: str(x).split(':')[0])
    acci['Hour'] = acci['Hour'].apply(pd.to_numeric, errors='coerce')
    hour = []
    num_of_fatal_acci = []
    num_of_acci = []
    for i in range(24):
        hour.append(i)
        num_of_fatal_acci_hour = len(acci[(acci['Accident_Severity']== 1) & (acci['Hour'] == i)])
        num_of_acci_hour = len(acci[acci['Hour'] == i])
        num_of_fatal_acci.append(num_of_fatal_acci_hour)
        num_of_acci.append(num_of_acci_hour)
        normalized_num_of_fatal_acci = list(np.array(num_of_fatal_acci) / np.array(num_of_acci) *100)
    fig = px.line(x=hour, y=normalized_num_of_fatal_acci, labels={'x':'Hour', 'y':'Percentage of fatal Accidents'})
    return fig

#gender
def gender():
    cf=pd.read_csv('C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Casualties0514.csv')
    men =len(cf[cf['Sex_of_Casualty']==1])
    women =len(cf[cf['Sex_of_Casualty']==2])
    x = ['Men', 'Women']
    y = [men,women]
    x_pos =list(range(len(x)))
    fig = px.bar(x=x, y=y , labels={'x':'Gender', 'y':'Casualties'})
    return fig

#graph
def accident_frequency():
    acci=pd.read_csv('C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Accidents0514.csv')
    acci['Year'] = acci['Accident_Index'].map(lambda x: str(x)[:4])
    acci['Year'] = acci['Year'].apply(pd.to_numeric, errors='coerce')
    year = []
    num_of_acci_year = []
    for i in range(2005, 2015):
        year.append(i)
        num_of_acci_year.append(len(acci[acci['Year'] == i]))
    fig = px.line(x=year, y=num_of_acci_year, labels={'x':'Year', 'y':'Number of Accidents'})
    return fig


#pie
def pieGraph():
    cf=pd.read_csv('C:/Users/PC-DELL/OneDrive/Desktop/DV J COMP/Datasets_DV/Casualties0514.csv')
    Severity1 =len(cf[cf['Casualty_Severity']==1])
    Severity2 =len(cf[cf['Casualty_Severity']==2])
    Severity3 =len(cf[cf['Casualty_Severity']==3])
    tot=Severity1+Severity2+Severity3;
    s1=(Severity1/tot)*100;
    s2=(Severity2/tot)*100;
    s3=(Severity3/tot)*100;

    fig = go.Figure(data=[go.Pie(labels=['Deaths','Minor Injuries','Major Injuries'], values=[s1,s2,s3], pull=[0.2,0, 0],hole=0.4,marker_colors = ['lightskyblue', 'yellowgreen', 'lightcoral'])])
    return fig
app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
html.Div([
    html.Div([
            html.Img(src=app.get_asset_url('Road.jpg'),
                     id = 'Road.jpg',
                     style={'height': '100px',
                            'width': 'auto',
                            'margin-bottom': '25px',
                            'border-radius': '20px'})


        ], className='one-third column'),

        
    html.Div([
            html.H3('Road Accidents', style={'margin-bottom': '0px', 'color': 'white'}),
            html.H5('UK ROAD ACCIDENTS IN 2005-2015', style={'margin-bottom': '0px', 'color': 'white'})
        
        ], className='one-half column', id = 'title'),

    html.Div([
            html.H6('Last Updated: ' + str(acci['Date'].iloc[-1]),
                    style={'color': 'orange'})

        ], className='one-third column', id = 'title1')

    ], id = 'header', className= 'row flex-display', style={'margin-bottom': '25px'}),

html.Div([
    html.Div([
            html.H6(children='Mohammed Muazz Zuberi',
                    style={'textAlign': 'center',
                           'color': 'white',
                            'fontSize': 25}),
            html.P(f"(20BCE0489)",
                    style={'textAlign': 'center',
                           'color': '#69DADB',
                           'fontSize': 20}),
            html.P('QUARTET',
                   style={'textAlign': 'center',
                          'color': '#69DADB',
                          'fontSize': 18,
                          'margin-top': '-18px'})

        ], className='create_container four columns'),

    html.Div([
            html.H6(children='Khushi Singhania',
                    style={'textAlign': 'center',
                           'color': 'white',
                            'fontSize': 25}),
            html.P(f"(20BCE0498)",
                    style={'textAlign': 'center',
                           'color': 'orange',
                           'fontSize': 20}),
            html.P('QUARTET',
                   style={'textAlign': 'center',
                          'color': 'orange',
                          'fontSize': 18,
                          'margin-top': '-18px'})
        ], className='create_container four columns'),

    html.Div([
             html.H6(children='Archisa Kumar',
                    style={'textAlign': 'center',
                           'color': 'white',
                           'fontSize': 25}),
            html.P(f"(20BCE0499)",
                    style={'textAlign': 'center',
                           'color': 'pink',
                           'fontSize': 20}),
            html.P('QUARTET',
                   style={'textAlign': 'center',
                          'color': 'pink',
                          'fontSize': 18,
                          'margin-top': '-18px'})
        ], className='create_container four columns'),

    html.Div([
             html.H6(children='Ved Purohit',
                    style={'textAlign': 'center',
                           'color': 'white',
                           'fontSize':25}),
            html.P(f"(20BCE0488)",
                    style={'textAlign': 'center',
                           'color': '#DD4A48',
                           'fontSize': 20}),
            html.P('QUARTET',
                   style={'textAlign': 'center',
                          'color': '#DD4A48',
                          'fontSize': 18,
                          'margin-top': '-18px'})

        ], className='create_container four columns'),

    ], className='row flex display'),

    #####1
html.Div([
    html.Div([
        html.Div([dcc.Graph(id='pie', figure=pieGraph())]),
            html.H6(
                children='Pie Chart',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            

        ], className='card_container three columns'),

    html.Div([
        html.Div([dcc.Graph(id='gender', figure=gender())]),
            html.H6(children='Bar Graph',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            
        ], className='card_container three columns'),

    html.Div([
        html.Div([dcc.Graph(id='graph', figure=accident_frequency())]), 
             html.H6(children='Line Graph',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            
        ], className='card_container three columns'),]),

####2
html.Div([
    html.Div([
        html.Div([dcc.Graph(id='line', figure=number_of_accidents())]),
            html.H6(children='Line Graph (1)',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            

        ], className='card_container three columns'),

    html.Div([
        html.Div([dcc.Graph(id='line1', figure=number_of_accidents1())]),
            html.H6(children='Line Graph (2)',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            
        ], className='card_container three columns'),

    html.Div([
        html.Div([dcc.Graph(id='line2', figure=number_of_accidents2())]), 
             html.H6(children='Line Graph (3)',
                    style={'textAlign': 'center',
                           'color': 'white'}),
            
        ], className='card_container three columns'),]),
    


])

if __name__ == '__main__':
    app.run_server(debug=False)

