
from app.utils import get_exchange_rate
from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.types import Message



router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Добрый день. Как вас зовут?")


@router.message()
async def send_rate(message: types.Message) -> None:
    course = get_exchange_rate()

    if course is not None:
        await message.reply(f"Рад знакомству, {message.text}! Курс доллара сегодня {course}")
    else:
        await message.answer("Сервер не отвечает, повторите попытку позже.")

