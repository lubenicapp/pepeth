import requests
import json
import os
from datetime import date, timedelta
from abc import ABC, abstractmethod


def token_value():
    r = requests.get(os.getenv('POLYGON_ENDPOINT') + 'v1' +
                     "/open-close/crypto/MATIC/USD/" +
                     str(date.today()) +
                     f"?apiKey={os.getenv('POLYGON_API_KEY')}")
    j = json.loads(r.text)
    return j['close']


def value_over_time(n, span):
    if span not in ['minute', 'hour', 'day', 'week', 'month', 'year']:
        return 'error'
    r = requests.get(os.getenv('POLYGON_ENDPOINT') + 'v2' +
                     f"/aggs/ticker/X:MATICUSD/range/1/{span}/" +
                     str(date.today() - timedelta(days=n)) + '/' + str(date.today()) +
                     '?adjusted=true&sort=asc&limit=120&' +
                     f"apiKey={os.getenv('POLYGON_API_KEY')}")
    j = json.loads(r.text)
    values = [x['o'] for x in j['results']]
    return json.dumps((values, min(values), max(values)))
