from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_API_KEY = getenv('TELEGRAM_BOT_API_KEY')
COINMARKETCAP_API_KEY = getenv('COINMARKETCAP_API_KEY')
COINMARKETCAP_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/'
