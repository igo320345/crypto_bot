from aiogram import Router
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from services.coinmarketcap_service import CoinMarketCapService

router = Router()
service = CoinMarketCapService()

@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@router.message(Command('top_coins'))
async def top_coins_handler(message: Message):
    # TODO
    pass

@router.message(Command('coin_info'))
async def coin_info(message: Message, command: CommandObject):
    coin = service.coin_info(command.args)
    if coin != None:
        coin_description = f'#{coin.rank} {coin.name} - {coin.symbol}\n\
        {coin.website_url}\nPrice: {coin.quote.price}\nMarker Dominance:\
        {coin.quote.market_cap_dominance}'
        await message.answer_photo(coin.logo_url, caption = coin_description)
    else:
        await message.answer('not found')