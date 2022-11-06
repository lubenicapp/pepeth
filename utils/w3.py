from web3 import Web3
from web3.middleware import geth_poa_middleware
import dotenv
import os

dotenv.load_dotenv()

rpc = os.getenv('RPC')

w3 = Web3(Web3.HTTPProvider(rpc))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
