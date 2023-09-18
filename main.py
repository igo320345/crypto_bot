import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from config import BOT_API_KEY
from coinmarketcap_service import CoinMarketCapService

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    service = CoinMarketCapService()
    top_coins = ''
    for coin in service.top_k_coins(10):
        top_coins += f'#{coin.rank} {coin.name}\n'
    await message.answer(top_coins)


async def main() -> None:
    bot = Bot(BOT_API_KEY, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())