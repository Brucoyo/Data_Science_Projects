## Final Project - House price visualization
## Author: Bruce Pei

# Data cleaning and prediction have already done by Jupyter notebook
# import data from saved files

import dash
import dash_core_components as dcc
import dash_html_components as html
import emoji
import pandas as pd
import plotly
from dash.dependencies import Input, Output
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='DesciuitV',api_key='Q1xpEcxmp80nvR9Cho16')

mapbox_access_token = 'pk.eyJ1IjoiZGVzY2l1aXR2IiwiYSI6ImNqcnZ1OWZ6MjA1eDYzeXBpOG5sZWd1NGcifQ.GQV-bvZFT62xzUBu2d4s6g'
map_style = "mapbox://styles/desciuitv/cjrwd4gn215au1ftfaphiuhhl"

df = pd.read_csv("all_data.csv")

my_text=['Name:' + Neighborhood +'<br>Price:' + str(SalePrice)
  for Neighborhood, SalePrice in zip(list(df['Neighborhood']), list(df['SalePrice'])) ]


# Add la and lo
df["latitude"] = df.Neighborhood.replace({'Blmngtn' : 42.062806,
                                        'Blueste' : 42.009408,
                                        'BrDale' : 42.052500,
                                        'BrkSide': 42.033590,
                                        'ClearCr': 42.025425,
                                        'CollgCr': 42.021051,
                                        'Crawfor': 42.025949,
                                        'Edwards': 42.022800,
                                        'Gilbert': 42.027885,
                                        'GrnHill': 42.000854,
                                        'IDOTRR' : 42.019208,
                                        'Landmrk': 42.044777,
                                        'MeadowV': 41.991866,
                                        'Mitchel': 42.031307,
                                        'NAmes'  : 42.042966,
                                        'NoRidge': 42.050307,
                                        'NPkVill': 42.050207,
                                        'NridgHt': 42.060356,
                                        'NWAmes' : 42.051321,
                                        'OldTown': 42.028863,
                                        'SWISU'  : 42.017578,
                                        'Sawyer' : 42.033611,
                                        'SawyerW': 42.035540,
                                        'Somerst': 42.052191,
                                        'StoneBr': 42.060752,
                                        'Timber' : 41.998132,
                                        'Veenker': 42.040106})
df["longitude"] = df.Neighborhood.replace(
                                               {'Blmngtn' : -93.639963,
                                                'Blueste' : -93.645543,
                                                'BrDale' : -93.628821,
                                                'BrkSide': -93.627552,
                                                'ClearCr': -93.675741,
                                                'CollgCr': -93.685643,
                                                'Crawfor': -93.620215,
                                                'Edwards': -93.663040,
                                                'Gilbert': -93.615692,
                                                'GrnHill': -93.643377,
                                                'IDOTRR' : -93.623401,
                                                'Landmrk': -93.646239,
                                                'MeadowV': -93.602441,
                                                'Mitchel': -93.626967,
                                                'NAmes'  : -93.613556,
                                                'NoRidge': -93.656045,
                                                'NPkVill': -93.625827,
                                                'NridgHt': -93.657107,
                                                'NWAmes' : -93.633798,
                                                'OldTown': -93.615497,
                                                'SWISU'  : -93.651283,
                                                'Sawyer' : -93.669348,
                                                'SawyerW': -93.685131,
                                                'Somerst': -93.643479,
                                                'StoneBr': -93.628955,
                                                'Timber' : -93.648335,
                                                'Veenker': -93.657032})


Neighborhood_list = list(map(str.upper, df.groupby('Neighborhood').size().index.tolist()))
Neighborhood_dict_list = []
Neighborhood_dict_list.append(dict(label = "All Neighborhood", value = "All Neighborhood"))
for Neighborhood in Neighborhood_list:
    Neighborhood_dict = dict(label = Neighborhood, value = Neighborhood)
    Neighborhood_dict_list.append(Neighborhood_dict)

# change Neightborhood to upper case
df['Neighborhood'] = df['Neighborhood'].str.upper()

# datetime
df["day"]="01"
df.rename(columns={'YrSold':'year','MoSold':'month'}, inplace=True)
df['datetime'] = pd.to_datetime(df[['year', 'month']].assign(Day=1))

# let's convert the datetime column to the appropriate type
df['datetime'] = pd.to_datetime(df['datetime'], errors = "coerce")


### Data visualization

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H4(emoji.emojize("House Price Prediction by Machine Learning :castle::house::derelict_house: - Bruce Pei ")),

    dcc.Tabs(id = "tabs", children = [
        dcc.Tab(label="Very few people are buying house in 2009 and 2010", children=[
            html.Div([

                html.Div(id="words", children=[

                    dcc.Graph(id='line-graph1')

                ], style={'width': '50%', 'str': 'top', 'display': 'inline-block','vertical-align':'top'}),

                html.Div(id="line-d", children=[
                    dcc.Graph(id='line-graph')
                ], style={'width': '50%', 'int': 'right', 'display': 'inline-block','vertical-align':'top'}),
            ]),

            html.Section([

                html.Div(["Year Range",
                          dcc.RangeSlider(id='year-slider1',
                                          min=df.datetime.dt.year.min(),
                                          max=df.datetime.dt.year.max(),
                                          value=[2006, 2010],
                                          marks={str(year): str(year) for year in df.datetime.dt.year.unique()[::4]}
                                          )
                          ], style={'width': '50%', 'float': 'right', 'display': 'inline-block', 'padding': 30,
                                    'padding-bottom': '35px'}),

                html.Div(["Select a Neighborhood",
                          dcc.Dropdown(id='Neighborhood-dropdown1',
                                       options=Neighborhood_dict_list,
                                       value='All Neighborhood',
                                       clearable=False)
                          ], style={'width': '25%', 'display': 'inline-block', 'padding-left': '10px',
                                    'padding-bottom': '10px'})
            ], style={'background-color': '#F9F9F9', 'border-radius': '15px'})
        ],
                selected_style={'borderLeft': '1px solid #d6d6d6',
                                'borderRight': '1px solid #d6d6d6',
                                'backgroundColor': '#001580',
                                'color': 'white'}),

        dcc.Tab(label = "More Houses sold in summer with barely price difference within the year", children = [

            html.Div([

                html.Div(id="bar-plot1", children=[
                     dcc.Graph(id='bar-p1')
                    ], style={'width': '50%', 'int': 'right', 'display': 'inline-block'}),

                html.Div(id="bar-plot", children=[
                        dcc.Graph(id='bar-p')
                    ], style={'width': '50%', 'int': 'right', 'display': 'inline-block'})
                        ]),
            html.Section([

                html.Div(["Year Range",
                          dcc.RangeSlider(id='year-slider',
                                          min=df.datetime.dt.year.min(),
                                          max=df.datetime.dt.year.max(),
                                          value=[2006, 2010],
                                          marks={str(year): str(year) for year in df.datetime.dt.year.unique()[::4]}
                                          )
                          ], style={'width': '50.75%', 'float': 'right', 'display': 'inline-block', 'padding': 30,
                                    'padding-bottom': '35px'}),

                html.Div(["Select a Neighborhood",
                          dcc.Dropdown(id='Neighborhood-dropdown',
                                       options=Neighborhood_dict_list,
                                       value='All Neighborhood',
                                       clearable=False)
                          ], style={'width': '25%', 'display': 'inline-block', 'padding-left': '10px',
                                    'padding-bottom': '10px'})
            ], style={'background-color':'#F9F9F9', 'border-radius': '15px'})
            ],
                selected_style={'borderTop': '1px solid #d6d6d6',
                               'borderBottom': '1px solid #d6d6d6',
                               'backgroundColor': '#001580',
                               'color': 'white'})

    ], style = {'height': '44px', 'borderBottom': '1px solid #d6d6d6', 'fontWeight': 'bold'})
], style={'width': '100%', 'display': 'inline-block'})

#########################################
#First tab# Callback
#########################################
@app.callback(Output('line-d', 'style'),
              [Input('Neighborhood-dropdown', 'value')])
def line_toggle_callback(Neighborhood_name):
    if(Neighborhood_name == "All Neighborhood"):
        return {'display': 'inline-block', 'width': '50%', 'int': 'left'}
    else:
        return {'display': 'inline-block', 'width': '50%', 'int': 'left'}

@app.callback(Output('line-graph', 'figure'),
              [Input('year-slider1', 'value'), Input('Neighborhood-dropdown1', 'value')])
def line_callback(slider_value, Neighborhood_name):
    start_year = int(slider_value[0])
    end_year = int(slider_value[1])
    subset_df = df[(df.datetime.dt.year >= start_year) & (df.datetime.dt.year <= end_year)]
    if(Neighborhood_name != "All Neighborhood"):
        subset_df = df[df.Neighborhood == Neighborhood_name]

    # let's group our data to see how the sightings vary by year
    year_data = subset_df.groupby(subset_df.datetime.dt.year).agg({"SalePrice": "mean"})
    line_trace = go.Scatter(x = year_data.index,
                            y = year_data["SalePrice"],
                            name = "House Price By year",
                            marker = dict(color = "blue", symbol = 'x'))
    traces = [line_trace]
    if(start_year == end_year):
        title = f"House Price in {start_year}"
    else:
        title = f"House Price between {start_year} - {end_year}"

    if(Neighborhood_name != "All Neighborhood"):
        title = title + f" in {Neighborhood_name}"

    layout = go.Layout(title = title,
                       xaxis = dict(title = "Year"),
                       yaxis = dict(title = "House Price $"))

    return dict(data = traces, layout = layout)


@app.callback(Output('line-graph1', 'figure'),
              [Input('year-slider1', 'value'), Input('Neighborhood-dropdown1', 'value')])
def line_callback(slider_value, Neighborhood_name):
    start_year = int(slider_value[0])
    end_year = int(slider_value[1])
    subset_df = df[(df.datetime.dt.year >= start_year) & (df.datetime.dt.year <= end_year)]
    if(Neighborhood_name != "All Neighborhood"):
        subset_df = df[df.Neighborhood == Neighborhood_name]

    # let's group our data to see how the sightings vary by year
    year_data = subset_df.groupby(subset_df.datetime.dt.year).agg({"SalePrice": "count"})
    line_trace = go.Scatter(x = year_data.index,
                            y = year_data["SalePrice"],
                            name = "House Price By year",
                            marker = dict(color = "blue", symbol = 'x'))
    traces = [line_trace]
    if(start_year == end_year):
        title = f"Number of House Sold in {start_year}"
    else:
        title = f"Number of House Sold between {start_year} - {end_year}"

    if(Neighborhood_name != "All Neighborhood"):
        title = title + f" in {Neighborhood_name}"

    layout = go.Layout(title = title,
                       xaxis = dict(title = "Year"),
                       yaxis = dict(title = "Total House Sold"))

    return dict(data = traces, layout = layout)


#########################################
#Second tab# Callback Oh! No second Tab
#########################################

@app.callback(Output('bar-plot1', 'style'),
              [Input('Neighborhood-dropdown', 'value')])
def line_toggle_callback(Neighborhood_name):
    if(Neighborhood_name == "All Neighborhood"):
        return {'display': 'inline-block', 'width': '50%', 'int': 'left'}
    else:
        return {'display': 'inline-block', 'width': '50%', 'int': 'left'}

@app.callback(Output('bar-p1', 'figure'),
              [Input('year-slider', 'value'), Input('Neighborhood-dropdown', 'value')])
def barplot_callback(slider_value, Neighborhood_name):

    start_year = int(slider_value[0])
    end_year = int(slider_value[1])
    subset_df = df[(df.datetime.dt.year >= start_year) & (df.datetime.dt.year <= end_year)]
    if(Neighborhood_name != "All Neighborhood"):
        subset_df = subset_df[subset_df.Neighborhood == Neighborhood_name]
    else:
        subset_df = subset_df

    # let's group our data to see how the sightings vary by month
    month_data = subset_df.groupby(subset_df.datetime.dt.month).agg({"SalePrice": "mean"})
    bar_trace = go.Bar(x = month_data.index,
                       y = month_data["SalePrice"],
                       name = "Average House Price by month",
                       marker = dict(color = ["#e28f5d" if month in (1, 6, 12) else
                                              "#6ce25d" if month in (2, 7, 11) else
                                              "#F4D03F" if month in (3, 9, 5) else
                                              "#635de2" for month in month_data.index]))
    traces = [bar_trace]

    if(start_year == end_year):
        title = f"Average House Price by month in {start_year}"
    else:
        title = f"Average House Price by month between {start_year} - {end_year}"

    if(Neighborhood_name != "All Neighborhood"):
        title = title + f" in {Neighborhood_name}"

    layout = go.Layout(title = title,
                       xaxis = dict(title = "Month",
                                    tickmode = "array",
                                    tickvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                    ticktext = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']),
                       yaxis = dict(title = "Average House Price"))

    return dict(data = traces, layout = layout)

@app.callback(Output('bar-plot', 'style'),
              [Input('Neighborhood-dropdown', 'value')])
def line_toggle_callback(Neighborhood_name):
    if(Neighborhood_name == "All Neighborhood"):
        return {'display': 'inline-block', 'width': '50%', 'int': 'left'}
    else:
        return {'display': 'inline-block', 'width': '50%', 'int': 'left'}

@app.callback(Output('bar-p', 'figure'),
              [Input('year-slider', 'value'), Input('Neighborhood-dropdown', 'value')])
def barplot_callback(slider_value, Neighborhood_name):

    start_year = int(slider_value[0])
    end_year = int(slider_value[1])
    subset_df = df[(df.datetime.dt.year >= start_year) & (df.datetime.dt.year <= end_year)]
    if(Neighborhood_name != "All Neighborhood"):
        subset_df = subset_df[subset_df.Neighborhood == Neighborhood_name]
    else:
        subset_df = subset_df

    # let's group our data to see how the sightings vary by month
    month_data = subset_df.groupby(subset_df.datetime.dt.month).agg({"SalePrice": "sum"})
    bar_trace = go.Bar(x = month_data.index,
                       y = month_data["SalePrice"],
                       name = "UFO sightings by month",
                       marker = dict(color = ["#e28f5d" if month in (1, 6, 12) else
                                              "#6ce25d" if month in (2, 7, 11) else
                                              "#F4D03F" if month in (3, 9, 5) else
                                              "#635de2" for month in month_data.index]))
    traces = [bar_trace]

    if(start_year == end_year):
        title = f"Total House Price by month in {start_year}"
    else:
        title = f"Total House Price by month between {start_year} - {end_year}"

    if(Neighborhood_name != "All Neighborhood"):
        title = title + f" in {Neighborhood_name}"

    layout = go.Layout(title = title,
                       xaxis = dict(title = "Month",
                                    tickmode = "array",
                                    tickvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                    ticktext = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']),
                       yaxis = dict(title = "House Sold Price"))

    return dict(data = traces, layout = layout)

if __name__ == '__main__':
    app.run_server(debug=True)