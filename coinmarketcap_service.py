from config import COINMARKETCAP_API_KEY
from coin import Coin
from requests import Session
import json


COINMARKETCAP_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }

def jsonConverter(data):
        return Coin(data['id'], data['name'], data['symbol'], data['cmc_rank'], data['quote'])
class CoinMarketCapService:
    
    def __init__(self):
        self.session = Session()
        self.session.headers.update(headers)

    def top_coins(self):
        response = self.session.get(COINMARKETCAP_API_URL + 'listings/latest')
        data = json.loads(response.text)
        result = []
        for coin_raw in data['data']:
            coin = jsonConverter(coin_raw)
            result.append(coin)
        return result