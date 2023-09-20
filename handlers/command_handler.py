from aiogram import Router
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from services.coinmarketcap_service import CoinMarketCapService

router = Router()
service = CoinMarketCapService()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@router.message(Command('top_coins'))
async def top_coins_handler(message: Message) -> None:
    top_coins = ''
    for coin in service.top_coins():
        top_coins += f'#{coin.rank} {coin.name}\n'
    await message.answer(top_coins)

@router.message(Command('coin_quotes'))
async def coin_quotes_handler(message: Message, command: CommandObject) -> None:
    coin = service.coin_quotes(command.args)
    await message.answer(f"#{coin.rank} {coin.name}\n{coin.quote['USD']['price']}")

@router.message(Command('coin_logo'))
async def coin_logo_handler(message: Message, command: CommandObject) -> None:
    coin_logo_url = service.coin_logo(command.args)
    await message.answer_photo(coin_logo_url)

@router.message(Command('coin_website'))
async def coin_website_handler(message: Message, command: CommandObject) -> None:
    coin_website_url = service.coin_website(command.args)
    await message.answer(coin_website_url)