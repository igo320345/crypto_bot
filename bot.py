import asyncio
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from handlers import command_handler
from config import BOT_API_KEY

async def main():
    bot = Bot(BOT_API_KEY, parse_mode = ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(command_handler.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())