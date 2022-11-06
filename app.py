from flask import Flask
from dotenv import load_dotenv
import os

from controllers.token_controller import TokenController
from controllers.polygon_api_controller import token_value, value_over_time

load_dotenv()

app = Flask(__name__)


@app.route('/token/market_cap')
def market_cap():
    return str(TokenController.market_cap())


@app.route('/token/total_supply')
def total_supply():
    return str(TokenController.total_supply())


@app.route('/token/current_value')
def current_value():
    return str(token_value())


@app.route('/token/value_over/<int:n>/day')
def historical_value(n):
    return value_over_time(n)


if __name__ == "__main__":
    app.run()
