class Quote:
    def __init__(self, price, volume_24h, percent_change_1h, percent_change_24h,
                 percent_change_7d, market_cap, market_cap_dominance):
        self.price = price
        self.volume_24h = volume_24h
        self.percent_change_1h = percent_change_1h
        self.percent_change_24h = percent_change_24h
        self.percent_change_7d = percent_change_7d
        self.market_cap = market_cap
        self.market_cap_dominance = market_cap_dominance

def quote_from_json(quotes):
    quotes = quotes['quote']['USD']
    return Quote(quotes['price'], quotes['volume_24h'], quotes['percent_change_1h'],
                 quotes['percent_change_24h'], quotes['percent_change_7d'],
                 quotes['market_cap'], quotes['market_cap_dominance'])
