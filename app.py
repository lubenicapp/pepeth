import dash
from dash import html
from dash_elements.graph import size_graph, time_graph, token_value_over_time
from dotenv import load_dotenv
import json
import numpy as np
from controllers.token_controller import TokenController
from controllers.polygon_api_controller import token_value, value_over_time
from controllers.block_controller import block_number, blocks_prop

SIZE = 100
DAYS = 180

app = dash.Dash(__name__)





app.layout = html.Div(
    children=[
        token_value_over_time(180),
        size_graph(SIZE, 'lines'),
        time_graph(SIZE, 'bar'),

    ]
)






if __name__ == "__main__":
    app.run_server(debug=True)
