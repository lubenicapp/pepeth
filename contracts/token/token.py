import json
from contracts.contract import Contract
from utils.w3 import w3

address = "0x0000000000000000000000000000000000001010"
with open("contracts/token/abi.json") as json_file:
    abi = json.load(json_file)

Token = Contract(address, abi=abi, w3=w3)
