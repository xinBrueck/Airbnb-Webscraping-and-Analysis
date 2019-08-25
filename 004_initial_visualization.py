import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

# Load data
df = data = pd.read_csv("./data/seattle_individual_listing_details.csv",
            sep='|', quotechar= '"', encoding= 'utf8')


# dtype = {'amendities': str, 'availableDts': str, 'id':str,
# 'listingHouseType':str, 'listingLoc': str, 'listingNm':str,
# 'neighborhoodSummary':str, 'numBaths':str, 'numBedrooms': str,
# 'numGuests' : str, 'price': str,
# 'numBeds': np.float64, 'reviewStar' : str, 'reviewTotal' : np.float64,
# 'listingHouseTypeGroup' : str, 'numBathNew': np.float64, 'sharedBath' : np.float64,
# 'numGuestsNew': np.float64, 'priceNew' : np.float64, 'availableDtsAug' : np.float64,
# 'availableDtsSep': np.float64, 'availableDtsNov':np.float64, 'amenityString':str,
# 'amenityBasic':str, 'amenityFamily':str, 'amenityFacilities':str, 'amenityDining':str,
# 'amenityAccess':str, 'amenityLogistics': str, 'amenityBB': str,
# 'amenitySafety':str, 'amenityNotIn': str},

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
                                    html.H5(
                                        "Filter by listing price range:",
                                        className="control_label",
                                    ),
                                    dcc.RangeSlider(
                                        id="price_slider",
                                        min=0,
                                        max=250,
                                        value= [0, 250],
                                        step = 50,
                                        marks={
                                            0: {'label': '$0'},
                                            50: {'label': '$50'},
                                            100: {'label': '$100'},
                                            150: {'label': '$150'},
                                            200: {'label': '$200'},
                                            250: {'label': '$250'}
                                        },
                                        className="dcc_control",
                                    ),

                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.H5("Choose the housing attribute:", className="control_label"),
                                    dbc.DropdownMenu(
                                        [
                                            dbc.DropdownMenuItem("House Type", id = '0'),
                                            dbc.DropdownMenuItem("Number of Beds", id = '1'),
                                            dbc.DropdownMenuItem("Number of Baths", id = '2'),
                                            dbc.DropdownMenuItem("Shared Bath", id = '3'),
                                            dbc.DropdownMenuItem("Number of Guests", id = '4'),
                                            dbc.DropdownMenuItem(divider=True),
                                            dbc.DropdownMenuItem("Number of Reviews", id = '5'),
                                            dbc.DropdownMenuItem("Review Rating", id = '6'),
                                            dbc.DropdownMenuItem(divider=True),
                                            dbc.DropdownMenuItem("Price", id = '7'),
                                        ],
                                        label="Housing Feature",
                                        color="success",
                                    )

                                ])
                            ])
                        ],
                        id="cross-filter-options",
                        width={"size": 3, "offset": 1},

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

if __name__ == '__main__':
    app.run_server(debug=True)
