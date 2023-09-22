from models.quote import quote_from_json
from multipledispatch import dispatch

class Coin:
    def __init__(self, id, name , symbol, rank, slug, quote = None, logo_url = '', website_url = ''):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.rank = rank
        self.slug = slug
        self.quote = quote
        self.logo_url = logo_url
        self.website_url = website_url

@dispatch(dict, dict)
def coin_from_json(quotes, info):
    quote = quote_from_json(quotes)
    return Coin(info['id'], info['name'], info['symbol'], quotes['cmc_rank'],
                 info['slug'], quote, info['logo'], info['urls']['website'][0])

@dispatch(dict)
def coin_from_json(info):
    return Coin(info['id'], info['name'], info['symbol'], info['cmc_rank'], info['slug'])
