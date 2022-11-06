### Pepeth

this is a work in progress

&nbsp;

#### Run the project

requirements : 

    - python3
    - a virtual env (ideally)

&nbsp;

to install dependencies, run

```bash 
pip install -r requirements.txt
```

&nbsp;


populate the `sample.env` with correct API keys and rename it `.env`

run the api with 
```bash
flask run
```

&nbsp;


#### API 

This tool extract data directly from the polygon blockchain through **JSON-RPC** and querying **smart contracts**.
It also gets data from external sources such as **polygon.io** api


Running the flask app will show in the terminal the local url to access the api. Probably http://127.0.0.1:5000

send get request to :

-  `/token/market_cap` to access the total market value (estimation)
-  `/token/total_supply` to access the total supply of token
-  `/token/current_value` to get the token value in $
-  `/token/value_over/n/days` to get the value over the last n days, and the min and max in this period

&nbsp;

- `/block/`
