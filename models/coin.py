from models.quote import quote_from_json

class Coin:
    def __init__(self, id, name , symbol, rank, quote, logo_url, website_url):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.rank = rank
        self.quote = quote
        self.logo_url = logo_url
        self.website_url = website_url

def coin_from_json(quotes, info):
    quote = quote_from_json(quotes)
    return Coin(info['id'], info['name'], info['symbol'], quotes['cmc_rank'],
                 quote, info['logo'], info['urls']['website'][0])
