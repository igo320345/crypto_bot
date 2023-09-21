from config import COINMARKETCAP_API_KEY, COINMARKETCAP_API_URL
from models.coin import coin_from_json
from requests import Session
import json

class CoinMarketCapService:
    def __init__(self):
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        }
        self.session = Session()
        self.session.headers.update(headers)

    def top_coins(self):
        # TODO
        pass
    
    def coin_info(self, coin_name: str):
        coin_name = coin_name.lower()
        params = {'slug': coin_name}
        response_quotes = self.session.get(COINMARKETCAP_API_URL + 'quotes/latest',
                                            params = params)
        response_info = self.session.get(COINMARKETCAP_API_URL + 'info',
                                            params = params)
        quotes = json.loads(response_quotes.text)
        info = json.loads(response_info.text)
        if quotes['status']['error_code'] != 0 or \
            info['status']['error_code'] != 0:
            return None
        quotes = list(quotes['data'].values())[0]
        info = info['data'][str(quotes['id'])]
        return coin_from_json(quotes, info)
        
        
