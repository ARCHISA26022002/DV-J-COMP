import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
import pandas as pd

def graph():
    vehi=pd.read_csv('Datasets DV/Vehicles0514.csv')
    age_acci = vehi[['Accident_Index', 'Age_of_Driver', 'Vehicle_Type']]
    age = []
    num_of_acci = []
    for i in range(17, max(age_acci['Age_of_Driver'])+1):
        age.append(i)
        num_of_acci.append(len(age_acci[(age_acci['Age_of_Driver']==i)&(age_acci['Vehicle_Type']== 9 )]))

    fig = px.line(x=age, y=num_of_acci, labels={'x':'Age', 'y':'Number of car accidents'})
    return fig

def pieGraph():
    cf=pd.read_csv('Datasets DV/Casualties0514.csv')
    Severity1 =len(cf[cf['Casualty_Severity']==1])
    Severity2 =len(cf[cf['Casualty_Severity']==2])
    Severity3 =len(cf[cf['Casualty_Severity']==3])
    tot=Severity1+Severity2+Severity3;
    s1=(Severity1/tot)*100;
    s2=(Severity2/tot)*100;
    s3=(Severity3/tot)*100;

    fig=px.pie(values=[s1,s2,s3],names=['Severity 1','Severity 2','Severity 3'],title='Casualty Severity')
    labels = 'Deaths','MajorInjuries','Minor Injuries'
    sizes = [s1, s2, s3]
    colors = ['lightskyblue', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)
    return fig


def bar_graph():
    acci=pd.read_csv('Datasets DV/Accidents0514.csv')
    cf=pd.read_csv('Datasets DV/Casualties0514.csv')
    vf=pd.read_csv('Datasets DV/Vehicles0514.csv')
    urban_acci =len(acci[acci['Urban_or_Rural_Area']==1])
    rural_acci =len(acci[acci['Urban_or_Rural_Area']==2])
    na_acci =len(acci[acci['Urban_or_Rural_Area']==3])
    total_acci = urban_acci + rural_acci + na_acci
    urban_pct = urban_acci / total_acci * 100
    rural_pct = rural_acci / total_acci *100
    na_pct = na_acci / total_acci * 100
    print("Percentage of accidents occur in urban areas is {0:.0f}%".format(urban_pct))
    print("Percentage of accidents occur in rural areas is {0:.0f}%".format(rural_pct))
    print("Percentage of accidents occur in other areas is {0:.0f}%".format(na_pct))
    x = ['Urban', 'Rural', 'Other']
    y = [urban_pct, rural_pct,na_pct]
    x_pos =list(range(len(x)))
    fig=px.bar(x=x,y=y,color=x,title='Urban, Rural, and Other Areas')
    return fig

def gender():
    cf=pd.read_csv('Datasets DV/Casualties0514.csv')
    men =len(cf[cf['Sex_of_Casualty']==1])
    women =len(cf[cf['Sex_of_Casualty']==2])
    x = ['Men', 'Women']
    y = [men,women]
    x_pos =list(range(len(x)))
    fig = px.bar(x=x, y=y)
    return fig

def accident_frequency():
    acci=pd.read_csv('Datasets DV/Accidents0514.csv')
    acci['Year'] = acci['Accident_Index'].map(lambda x: str(x)[:4])
    acci['Year'] = acci['Year'].apply(pd.to_numeric, errors='coerce')
    year = []
    num_of_acci_year = []
    for i in range(2005, 2015):
        year.append(i)
        num_of_acci_year.append(len(acci[acci['Year'] == i]))
    fig = px.line(x=year, y=num_of_acci_year, labels={'x':'Year', 'y':'Number of Accidents'})
    return fig

def fatal_accidents():
    cf=pd.read_csv('Datasets DV/Casualties0514.csv')
    fatal =len(cf[cf['Casualty_Severity']==3])
    non_fatal =len(cf[cf['Casualty_Severity']==2])
    x = ['Fatal', 'Non-Fatal']
    y = [fatal,non_fatal]
    x_pos =list(range(len(x)))
    fig = px.line(x=x, y=y)
    return fig

def number_of_accidents():
    acci=pd.read_csv('Datasets DV/Accidents0514.csv')
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
    fig = px.line(x=hour, y=normalized_num_of_fatal_acci, labels={'x':'Hour', 'y':'Percentage of Fatal Accidents'})
    return fig






app = dash.Dash(__name__)
app.layout = html.Div([html.H1('Dashboard' , style={'textAlign': 'center'}),
html.H2('Analysis on Road Accidents', style={'textAlign': 'center'}),
html.Div([dcc.Graph(id='graph', figure=graph()), 
dcc.Graph(id='pie', figure=pieGraph()), 
dcc.Graph(id='bar', figure=bar_graph()), 
dcc.Graph(id='noa', figure=number_of_accidents()),
dcc.Graph(id='gender',figure=gender())])
]) 


app.run_server()