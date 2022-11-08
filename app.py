from flask import Flask
from dotenv import load_dotenv
import json
import numpy as np
from controllers.token_controller import TokenController
from controllers.polygon_api_controller import token_value, value_over_time
from controllers.block_controller import block_number, blocks_prop

load_dotenv()

app = Flask(__name__)


@app.route('/token/market_cap')
def market_cap():
    return json.dumps({'market_cap': TokenController.market_cap()})


@app.route('/token/total_supply')
def total_supply():
    return json.dumps({'total_supply': TokenController.total_supply()})


@app.route('/token/current_value')
def current_value():
    return json.dumps({'value': token_value()})


@app.route('/token/value_over/<int:n>/day')
def historical_value(n):
    return value_over_time(n)


@app.route('/block/number')
def latest_block_number():
    return json.dumps({'last_block': block_number()})


@app.route('/block/last/<int:n>/size')
def last_blocks_sizes(n):
    return blocks_prop(n, 'size')

@app.route('/block/last/<int:n>/time')
def last_blocks_times(n):
    values = np.diff(blocks_prop(n, 'timestamp')['timestamp'])
    return json.dumps({'time': [int(x) for x in values]})


if __name__ == "__main__":
    app.run()
