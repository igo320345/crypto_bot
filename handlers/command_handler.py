from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from handlers import coin_info_handler, top_coins_handler

router = Router()
router.include_routers(coin_info_handler.router, top_coins_handler.router)

@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!\n/top_coins - Top cryptocurrencies by market cap\n/coin_info - Cryptocurrency description and quotes")
