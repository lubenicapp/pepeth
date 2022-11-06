from contracts.token.token import Token
from abc import ABC, abstractmethod
from controllers.polygon_api_controller import token_value

class TokenController(ABC):

    @abstractmethod
    def market_cap():
        supply = TokenController.total_supply()
        value = token_value()
        return supply * value

    @abstractmethod
    def total_supply():
        return Token.readonly_call('totalSupply') * 10 ** (-Token.readonly_call('decimals'))
