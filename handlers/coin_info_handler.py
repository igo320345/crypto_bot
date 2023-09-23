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
        coin_description = f'#{coin.rank} {hbold(coin.name)} - {coin.symbol}\n{coin.website_url}\nPrice: {coin.quote.price}\nMarker Dominance: {coin.quote.market_cap_dominance}'
        await message.answer_photo(coin.logo_url, caption = coin_description)
    else:
        await message.answer('not found')
    
