import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import main_handlers, number_tools, text_tools


load_dotenv()
API = os.getenv("API_TOKEN")

bot = Bot(API)
dp = Dispatcher()


async def main():

    dp.include_router(main_handlers.router)
    dp.include_router(number_tools.router)
    dp.include_router(text_tools.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
