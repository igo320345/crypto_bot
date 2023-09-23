from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.top_coins_keyboard import coin_list_keyboard
from services.coinmarketcap_service import CoinMarketCapService
from handlers.coin_info_handler import coin_info

router = Router()
service = CoinMarketCapService()
user_data = {}

@router.message(Command('top_coins'))
async def top_coins_handler(message: Message):
    user_data[message.from_user.id] = 10
    coin_list = service.top_coins(10)
    await message.answer('Top cryptocurrencies by market cap:',
                          reply_markup=coin_list_keyboard(coin_list))

async def update_coin_list(message: Message, amount: int):
    coin_list = service.top_coins(amount)
    await message.edit_text('Top cryptocurrencies by market cap:',
                            reply_markup=coin_list_keyboard(coin_list))
    
@router.callback_query(F.data == 'load_more')
async def load_more_callback(callback: CallbackQuery):
    amount = user_data.get(callback.from_user.id, 10)
    user_data[callback.from_user.id] = amount + 10
    await update_coin_list(callback.message, amount + 10)

@router.callback_query(F.data.startswith('coin_info'))
async def coin_info_callback(callback: CallbackQuery):
    coin = callback.data.split('_')[2]
    await coin_info(callback.message, coin)