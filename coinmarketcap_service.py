from config import COINMARKETCAP_API_KEY, COINMARKETCAP_API_URL
from coin import Coin
from requests import Session
import json

class CoinMarketCapService:

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }
    
    def __init__(self):
        self.session = Session()
        self.session.headers.update(self.headers)

    def top_k_coins(self, k):
        params = {'limit': k, 'sort': 'cmc_rank'}
        response = self.session.get(COINMARKETCAP_API_URL + 'cryptocurrency/map', 
                                    params = params)
        data = json.loads(response.text)
        result = []
        for coin in data['data']:
            result.append(Coin(**coin))
        return result