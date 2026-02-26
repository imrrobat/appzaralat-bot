from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from utils import START_MESSAGE, HELP_MESSAGE

router = Router()


@router.message(CommandStart())
async def start_handler(pm: Message):
    await pm.answer(START_MESSAGE)


@router.message(Command("help"))
async def help_handler(pm: Message):
    await pm.answer(HELP_MESSAGE)
