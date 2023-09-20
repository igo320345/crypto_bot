import asyncio
from aiogram import Bot, Dispatcher
from handlers import command_handler
from config import BOT_API_KEY

async def main():
    bot = Bot(BOT_API_KEY)
    dp = Dispatcher()

    dp.include_routers(command_handler.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())