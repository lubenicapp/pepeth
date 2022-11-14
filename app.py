# Import modules
import dash
from dash import dcc, html
from dash_elements.graph import size_graph, time_graph, token_value_over_time
from dotenv import load_dotenv
import json
import numpy as np
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from controllers.token_controller import TokenController
from controllers.polygon_api_controller import token_value, value_over_time
from controllers.block_controller import block_number, blocks_prop

SIZE = 100
DAYS = 365

# Initiate the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP])

#colours
colors = {
    'black' : '#1A1B25',
    'red' : '#F8C271E',
    'white' : '#EFE9E7',
    'background' : '#333333',
    'text' : '#FFFFFF'
}


# Build the components
header_component = html.H1("PEPETH : A Polygon Block Explorer", className = "text-center p-2", style = {'color': '#EFE9E7'}),
under_header_component = html.H5("Check out the latest stats", className = "text-center p-2", style = {'color': '#EFE9E7'}),
text_token_val = html.P("Token value", className="text-center"),
text_block_n = html.P("Block count", className="text-center")

# Graphs
token = html.Div(token_value_over_time(365), style={'backgroundColor' : colors['background']}),
size = size_graph(SIZE, 'lines'),
time = time_graph(SIZE, 'lines'),
        # time_graph(SIZE, 'bar'),
block_n = html.Span(block_number(), className="border rounded-top d-flex justify-content-center bg-light border mb-2"),
token_val = html.Span(token_value(), className="border rounded-top position-relative text-center d-flex justify-content-center bg-light border mb-2"),
# total_supply = total_supply(),
# market_cap = market_cap(),



#navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("How it works", href="#"),
                dbc.DropdownMenuItem("The statistics", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Explore",
        ),
    ],
    brand="PEPETH",
    brand_href="#",
    color="dark",
    dark=True,
)

# Jumbotron
jumbotron = html.Div(
    dbc.Container(
        [
    
            html.H1("PEPETH", className="display-2 text-center"),
            html.P(
                "A POLYGON BLOCK EXPLORER",
                className="lead text-center",
            ),
            html.Hr(className="my-2 text-center"),
            html.P(
                "The place to find all Polygon statistics",
                className="text-center"
            ),
            html.P(
                dbc.Button("Learn more", color="primary"), className="lead text-center text-center"
            ),
        
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)




# Design the layout
app.layout = html.Div(style={'background': colors['background']}, children=[
    
        navbar, 
        
        jumbotron,
     

        dbc.Row(
             under_header_component
         ),


         dbc.Row(
            [dbc.Col(
                text_token_val
                ), 
            
            dbc.Col(
               text_block_n
                ),
            
            dbc.Col(
                text_block_n
                ) 
            ]
        ),


        dbc.Row(
            [dbc.Col(
                token_val,              
                ), 

            
            dbc.Col(
                block_n
                ),
            
            dbc.Col(
                block_n
                ) 
            ]
        ),
        


         
        dbc.Row(
            [dbc.Col(
                token
                ), 
            
            dbc.Col(
                size
                ) 
            ]
        ),
        
        # dbc.Row(
        # [dbc.Col(), dbc.Col()]
        # ),
    html.Div("PEPETH 2022", className="fixed-bottom bg-primary text-white text-center")
    
     ]


)




# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
