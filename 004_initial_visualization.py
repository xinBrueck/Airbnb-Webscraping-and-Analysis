import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import pandas as pd
import numpy as np

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

# define column types
colTypes = {
'amendities' :str,
'availableDts' :str,
'id' : str,
'listingHouseType' :str,
'listingLoc' :str,
'listingNm' : str,
'neighborhoodSummary' :str,
'numBaths' :  str,
'numBedrooms' : str,
'numBeds' :  np.float64,
'numGuests' : str,
'price' :     str,
'reviewStar' : np.float64,
'reviewTotal' :np.float64,
'listingHouseTypeGroup': str,
'numBathNew' : np.float64,
'sharedBath' : np.float64,
'numGuestsNew' :   np.float64,
'priceNew' : np.float64,
'availableDtsAug' :np.float64,
'availableDtsSep' :np.float64,
'availableDtsOct' :np.float64,
'amenityString' :   str,
'amenityBasic' :str,
'amenityFamily' :   str,
'amenityFacilities' :  str,
'amenityDining' :   str,
'amenityAccess' :   str,
'amenityLogistics' :str,
'amenityBB' : str,
'amenitySafety' :   str,
'amenityNotIn' :str,
'totalAvailableDts' : np.float64
}
# Load data
dt = pd.read_csv("./data/seattle_individual_listing_details_cleaned.csv", sep='|', quotechar= '"',
encoding= 'utf8', index_col=0, dtype = colTypes)

##set the type for each attributes


##define glable varialbles

NUMERIC_FEATURES = ['P', 'NR', 'TAD']
CATEGORICAL_FEATURES = ['HT', 'NBe', 'NBa', 'SB', 'NG', 'RR']
COLNAME_DIST = {
    'P': 'priceNew',
    'NR': 'reviewTotal',
    'TAD': 'totalAvailableDts',
    'HT':'listingHouseTypeGroup',
    'NBed': 'numBeds',
    'NBer': 'numBedrooms',
    'NBa': 'numBathNew',
    'SB': 'sharedBath',
    'RR':'reviewStar',
    'NG': 'numGuestsNew'
}

LABEL_DIST = {
    'P': 'Lising Price',
    'NR': 'Number of Reviews',
    'TAD': 'Total Available Dates',
    'HT':'Housing Type',
    'NBed': 'Number of Beds',
    'NBer': 'Number of Bedrooms',
    'NBa': 'Number of Bath',
    'SB': 'Shared Bath',
    'RR':'Review Ratings',
    'NG': 'Number of Guests'
}

# Create app layout
app.layout = html.Div(
    [
        dbc.Container([
            dbc.Row([
                html.H1(
                    "Airbnb Housing Listing Analysis",
                ),
                ],
                id="header",
                justify="center",
            ),

            dbc.Row([
                html.H5(
                    "Attribute Explore",
                ),
            ],
            justify="center",
            style={"margin-bottom": "100px"},)
        ], fluid=True),
        dbc.Container(
            [
                dbc.Row([
                    dbc.Col(
                        [
                            dbc.Card([
                                dbc.CardBody([
                                    html.H5("Choose the housing attribute: X, Y, Z", className="control_label"),
                                    dcc.Dropdown(
                                        id='drop-down-x',
                                        options=[
                                            {'label': 'House Type', 'value': 'HT'},
                                            {'label': 'Number of Beds', 'value': 'NBed'},
                                            {'label': 'Number of Bedrooms', 'value': 'NBer'},
                                            {'label': 'Number of Baths', 'value': 'NBa'},
                                            {'label': 'Shared Bath', 'value': 'SB'},
                                            {'label': 'Number of Guests', 'value': 'NG'},
                                            {'label': 'Number of Reviews', 'value': 'NR'},
                                            {'label': 'Review Ratings', 'value': 'RR'},
                                            {'label': 'Price', 'value': 'P'},
                                            {'label': 'Total Available Dates', 'value': 'TAD'},
                                        ],
                                        value='HT'
                                    ),

                                    html.Br(),

                                    dcc.Dropdown(
                                        id='drop-down-y',
                                        options=[
                                            {'label': 'House Type', 'value': 'HT'},
                                            {'label': 'Number of Beds', 'value': 'NBed'},
                                            {'label': 'Number of Bedrooms', 'value': 'NBer'},
                                            {'label': 'Number of Baths', 'value': 'NBa'},
                                            {'label': 'Shared Bath', 'value': 'SB'},
                                            {'label': 'Number of Guests', 'value': 'NG'},
                                            {'label': 'Number of Reviews', 'value': 'NR'},
                                            {'label': 'Review Ratings', 'value': 'RR'},
                                            {'label': 'Price', 'value': 'P'},
                                            {'label': 'Total Available Dates', 'value': 'TAD'},
                                        ],
                                        value='P'
                                    ),

                                    html.Br(),

                                    dcc.Dropdown(
                                        id='drop-down-z',
                                        options=[
                                            {'label': 'House Type', 'value': 'HT'},
                                            {'label': 'Number of Beds', 'value': 'NBed'},
                                            {'label': 'Number of Bedrooms', 'value': 'NBer'},
                                            {'label': 'Number of Baths', 'value': 'NBa'},
                                            {'label': 'Shared Bath', 'value': 'SB'},
                                            {'label': 'Number of Guests', 'value': 'NG'},
                                            {'label': 'Number of Reviews', 'value': 'NR'},
                                            {'label': 'Review Ratings', 'value': 'RR'},
                                            {'label': 'Price', 'value': 'P'},
                                            {'label': 'Total Available Dates', 'value': 'TAD'},
                                        ],
                                        value='NBer'
                                    ),

                                ])
                            ])
                        ],
                        id="cross-filter-options",
                        width={"size": 2, "offset": 1},

                    ),
                    dbc.Col(
                        [
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div(
                                        [dcc.Graph(id="attribute_graph")],
                                        id="attributeGraphContainer",
                                        className="pretty_container",
                                    ),
                                ])
                            ])

                        ],
                        id="right-column",
                    ),
                ])
            ],
            className="mt-4",
            fluid=True
        ),
    ],
    id="mainContainer")

##make graphs
@app.callback(
    Output('attribute_graph', 'figure'),
    [Input('drop-down-x', 'value'),
     Input('drop-down-y', 'value'),
     Input('drop-down-z', 'value')])

def update_figure(feature_x, feature_y, feature_z):

    data = [go.Scatter(
        x=dt[dt[COLNAME_DIST[feature_z]]==type][COLNAME_DIST[feature_x]],
        y=dt[dt[COLNAME_DIST[feature_z]]==type][COLNAME_DIST[feature_y]],
        text=type,
        mode='markers',
        opacity=0.8,
        marker={
            'size': 10,
            'line': {'width': 2, 'color': 'rgba(152, 0, 0, .8)'}
        },
        name=str(type)
    ) for type in dt[COLNAME_DIST[feature_z]].unique()
    ]


    # scatters = go.Scatter(
    #     x=dt[COLNAME_DIST[feature_x]],
    #     y=dt[COLNAME_DIST[feature_y]],
    #     mode='markers',
    #     marker={
    #         'size': 10,
    #         'color' : 'rgba(255, 182, 193, .9)',
    #         'line': {'width': 2, 'color': 'rgba(152, 0, 0, .8)'}
    #     }
    # )

    if feature_x in NUMERIC_FEATURES:
        layout = go.Layout(
            xaxis={
                'title': LABEL_DIST[feature_x],
            },
            yaxis={
                'title': LABEL_DIST[feature_y],
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    else: #get the mean for each categorical group
        average_by_group = dt.groupby([COLNAME_DIST[feature_x]]).agg({COLNAME_DIST[feature_y]: np.mean}).reset_index()

        lineOfBestFit = go.Scatter(
            x=average_by_group[COLNAME_DIST[feature_x]],
            y=average_by_group[COLNAME_DIST[feature_y]],
            mode='lines',
            showlegend = False,
        )

        layout = go.Layout(
            xaxis={
                'title': LABEL_DIST[feature_x],
                'categoryorder': 'array',
                'categoryarray': average_by_group[COLNAME_DIST[feature_x]]
            },
            yaxis={
                'title': LABEL_DIST[feature_y],
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )

        data.append(lineOfBestFit)




    return {
        'data': data,
        'layout':layout
    }


if __name__ == '__main__':
    app.run_server(debug=True, port = 8069)
