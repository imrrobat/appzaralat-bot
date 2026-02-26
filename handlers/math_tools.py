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


def convert_digits(text: str):
    fa_to_en = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
    en_to_fa = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

    if any(ch.isdigit() for ch in text):
        return text.translate(en_to_fa)

    if any(ch in "۰۱۲۳۴۵۶۷۸۹" for ch in text):
        return text.translate(fa_to_en)

    return text


@router.message(Command("number"))
async def number_command(message: Message):
    parts = message.text.split("\n", 1)

    if len(parts) < 2:
        await message.answer("فرمت:\n/number\n123")
        return

    text = parts[1].strip()
    converted = convert_digits(text)

    await message.answer(converted)
