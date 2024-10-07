import logging
import asyncio
from aiogram import Bot, Dispatcher
from env import TgKeys
from app.handler import router


bot = Bot(TgKeys.TOKEN)
dp = Dispatcher()


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING, filename="bot_logs.log",filemode="w")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
