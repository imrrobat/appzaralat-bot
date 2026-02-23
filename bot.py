import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

from utils import START_MESSAGE
from utils import percent_pattern

load_dotenv()
API = os.getenv("API_TOKEN")

bot = Bot(API)
dp = Dispatcher()


async def start_handler(pm: Message):
    await pm.answer(START_MESSAGE)


async def percent_handler(message: Message):
    text = message.text

    match = percent_pattern.match(text)
    if not match:
        return

    total = int(match.group(1))
    percent = int(match.group(2))

    result = total * percent / 100

    await message.answer(f"{percent}٪ از {total:,} میشه {result:,.0f}")


async def main():
    dp.message.register(start_handler, CommandStart())
    dp.message.register(percent_handler, Command("darsad"))

    dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
