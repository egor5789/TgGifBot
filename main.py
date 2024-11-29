import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.methods import set_chat_menu_button

from handlers import user_handlers, functional_handlers
from states import storage
from config import load_config
from keyboards import MainMenuButton


async def main():

    """ Питонячий скрипт"""

    bot = Bot(
        token=load_config().tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher(storage=storage)
    dp.include_routers(
        user_handlers.router,
        functional_handlers.router
    )

    await bot.delete_webhook(drop_pending_updates=True)

    dp.startup.register(MainMenuButton.set_commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())