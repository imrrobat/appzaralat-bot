import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from handlers import math_tools

from utils import START_MESSAGE


load_dotenv()
API = os.getenv("API_TOKEN")

bot = Bot(API)
dp = Dispatcher()


async def start_handler(pm: Message):
    await pm.answer(START_MESSAGE)


async def main():
    dp.message.register(start_handler, CommandStart())

    dp.include_router(math_tools.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
