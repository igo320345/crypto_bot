from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from services.coinmarketcap_service import CoinMarketCapService

class CoinInfoState(StatesGroup):
    entering_coin_name = State()

router = Router()
service = CoinMarketCapService()

@router.message(Command('coin_info'))
async def coin_info_handler(message: Message, state: FSMContext):
    await message.answer('Enter cryptocurrency name: ')
    await state.set_state(CoinInfoState.entering_coin_name)

@router.message(CoinInfoState.entering_coin_name)
async def entered_coin_name(message: Message, state: FSMContext):
    await coin_info(message, message.text.lower())
    await state.clear()

async def coin_info(message: Message, coin: str):
    coin = service.coin_info(coin)
    if coin != None:
        percent_change_1h = f'Percent change 1h : {"🟩" if coin.quote.percent_change_1h > 0 else "🟥"} {coin.quote.percent_change_1h}'
        percent_change_24h = f'Percent change 24h : {"🟩" if coin.quote.percent_change_24h > 0 else "🟥"} {coin.quote.percent_change_24h}'
        percent_change_7d = f'Percent change 7d : {"🟩" if coin.quote.percent_change_7d > 0 else "🟥"} {coin.quote.percent_change_7d}'
        quote = f'Price: {coin.quote.price}\nMarket Cap: {coin.quote.market_cap}\nMarket Dominance: {coin.quote.market_cap_dominance}\n{percent_change_1h}\n{percent_change_24h}\n{percent_change_7d}\nVolume 24h: {coin.quote.volume_24h}'
        coin_description = f'#{coin.rank} {hbold(coin.name)} - {coin.symbol}\n{coin.website_url}\n{quote}'
        await message.answer_photo(coin.logo_url, caption = coin_description)
    else:
        await message.answer('not found')
    
