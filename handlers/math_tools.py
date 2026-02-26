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
    fa_digits = "۰۱۲۳۴۵۶۷۸۹"
    en_digits = "0123456789"

    fa_to_en = str.maketrans(fa_digits, en_digits)
    en_to_fa = str.maketrans(en_digits, fa_digits)

    has_fa = any(ch in fa_digits for ch in text)
    has_en = any(ch in en_digits for ch in text)

    if has_fa and not has_en:
        return text.translate(fa_to_en)

    if has_en and not has_fa:
        return text.translate(en_to_fa)

    return text.translate(fa_to_en).translate(en_to_fa)


@router.message(Command("number"))
async def number_command(message: Message):
    parts = message.text.split("\n", 1)

    if len(parts) < 2:
        await message.answer("فرمت:\n/number\n123")
        return

    text = parts[1].strip()
    converted = convert_digits(text)

    await message.answer(converted)
