import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from bot import handlers
from bot.dispatcher import dp
from env_data.utils import Env


async def all_middleware():
    pass


async def main() -> None:
    i18n = I18n(path='locales', default_locale='en', domain="message")
    bot = Bot(token=Env.bot.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.update.middleware(FSMI18nMiddleware(i18n))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())