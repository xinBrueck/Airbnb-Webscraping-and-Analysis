import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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


layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    mapbox=dict(
        # accesstoken=mapbox_access_token,
        style="light",
        center=dict(lon=-78.05, lat=42.54),
        zoom=7,
    ),
)
# Create app layout
app.layout = html.Div(
    [
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Airbnb Housing Listing Analysis",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Attribute Explore", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.P(
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
                                250: {'label': '$0'},
                                50: {'label': '$50'},
                                100: {'label': '$100'},
                                150: {'label': '$150'},
                                200: {'label': '$200'},
                                250: {'label': '$250'}
                            },
                            className="dcc_control",
                        ),

                        html.P("Choose the housing attribute:", className="control_label"),
                        dcc.Dropdown(
                            id="attribute_dropdown",
                            options=[
                                {'label': 'Number of Beds', 'value': 'NBe'},
                                {'label': 'Number of Baths', 'value': 'NBa'},
                                {'label': 'Shared Baths', 'value': 'SB'},
                                {'label': 'Number of Guests', 'value': 'NG'},
                                {'label': 'Price', 'value': 'P'},
                                {'label': 'Number of Reviews', 'value': 'NR'},
                                {'label': 'Review Stars', 'value': 'RS'},
                                {'label': 'House Type', 'value': 'HT'},
                                {'label': 'Number of Reviews', 'value': 'NR'},
                                {'label': 'Review Stars', 'value': 'RS'},
                                {'label': 'House Type', 'value': 'HT'},
                            ],
                            className="dcc_control",
                        ),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",

                ),
                html.Div(
                    [
                        html.Div(
                            [
                        html.Div(
                            [dcc.Graph(id="count_graph")],
                            id="countGraphContainer",
                            className="pretty_container",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",

        ),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
),
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
