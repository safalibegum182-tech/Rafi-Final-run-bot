import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot import router, auto_loop
from config import settings

logging.basicConfig(level=logging.INFO)

async def main():
    if not settings.bot_token:
        raise RuntimeError("BOT_TOKEN is missing. Add it in Railway Variables.")
    bot = Bot(settings.bot_token)
    dp = Dispatcher()
    dp.include_router(router)
    asyncio.create_task(auto_loop(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
