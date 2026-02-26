import re
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

ZWNJ = "\u200c"


def fix_zwnj(text: str):
    text = re.sub(r"\b(ن?می)\s+", r"\1" + ZWNJ, text)
    text = re.sub(r"\s+ها\b", ZWNJ + "ها", text)
    text = re.sub(r"\s+(تر|ترین)\b", ZWNJ + r"\1", text)

    return text


@router.message(Command("nim"))
async def zwnj_command(message: Message):
    parts = message.text.split("\n", 1)

    if len(parts) < 2:
        await message.answer("فرمت:\n/zwnj\nمی رود خانه ها بزرگ تر")
        return

    text = parts[1].strip()
    fixed = fix_zwnj(text)

    await message.answer(fixed)
