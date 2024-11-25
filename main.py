import asyncio
from aiogram import Bot, Dispatcher

import handlers


async def main():
    BOT_TOKEN = '6125202965:AAEmJ7Pv5Znr71GwcPuzWPPXk8IK89ZFEuw'
    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()
    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())