from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from services.coinmarketcap_service import CoinMarketCapService
from keyboards.top_coins_keyboard import coin_list_keyboard

class CoinInfoState(StatesGroup):
    entering_coin_name = State()

router = Router()
service = CoinMarketCapService()

user_data = {}

@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!\n/top_coins - Top cryptocurrencies by market cap\n/coin_info - Cryptocurrency description and quotes")

@router.message(Command('top_coins'))
async def top_coins_handler(message: Message):
    user_data[message.from_user.id] = 10
    coin_list = service.top_coins(10)
    await message.answer('Top cryptocurrencies by market cap:',
                          reply_markup=coin_list_keyboard(coin_list))

@router.message(Command('coin_info'))
async def coin_info_handler(message: Message, state: FSMContext):
    await message.answer('Enter cryptocurrency name: ')
    await state.set_state(CoinInfoState.entering_coin_name)

@router.message(CoinInfoState.entering_coin_name)
async def entered_coin_name(message: Message, state: FSMContext):
    await coin_info(message, message.text.lower())
    await state.clear()

async def update_coin_list(message: Message, amount: int):
    coin_list = service.top_coins(amount)
    await message.edit_text('Top cryptocurrencies by market cap:',
                            reply_markup=coin_list_keyboard(coin_list))

async def coin_info(message: Message, coin: str):
    coin = service.coin_info(coin)
    if coin != None:
        coin_description = f'#{coin.rank} {hbold(coin.name)} - {coin.symbol}\n{coin.website_url}\nPrice: {coin.quote.price}\nMarker Dominance: {coin.quote.market_cap_dominance}'
        await message.answer_photo(coin.logo_url, caption = coin_description)
    else:
        await message.answer('not found')
    
@router.callback_query(F.data == 'load_more')
async def load_more_callback(callback: CallbackQuery):
    amount = user_data.get(callback.from_user.id, 10)
    user_data[callback.from_user.id] = amount + 10
    await update_coin_list(callback.message, amount + 10)

@router.callback_query(F.data.startswith('coin_info'))
async def coin_info_callback(callback: CallbackQuery):
    coin = callback.data.split('_')[2]
    await coin_info(callback.message, coin)