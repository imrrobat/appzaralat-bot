from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils import percent_pattern

router = Router()


@router.message(Command("darsad"))
async def percent_handler(message: Message):
    text = message.text.split("\n", 1)

    if len(text) < 2:
        await message.answer("فرمت درست: \n/darsad\n2000000%5")
        return

    data = text[1].strip()

    match = percent_pattern.match(data)
    if not match:
        await message.answer("فرمت نامعتبره ❌")
        return

    total = int(match.group(1))
    percent = int(match.group(2))

    result = total * percent / 100

    await message.answer(f"{percent}٪ از {total:,} میشه {result:,.0f}")
