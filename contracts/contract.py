class Contract:

    def __init__(self, address, abi, w3):
        self.w3 = w3
        address = self.w3.toChecksumAddress(address)
        self.contract = self.w3.eth.contract(address, abi=abi)

    def readonly_call(self, function_name, *args):
        result = 0
        try:
            result = self.contract.functions[function_name](*args).call()
        except Exception as ex:
            print(ex)
        return result
