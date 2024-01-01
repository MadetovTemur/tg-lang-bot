# -*- coding: utf-8 -*-
import logging
from aiogram import executor

from loader import dp, db
from config import CFG
import misc, middlewares, handlers

async def on_startup(dispatcher):
    global CFG
    await db.create_tables()
    bot = await dp.bot.get_me()
    CFG['info']['bot_id'] = bot.id
    CFG['info']['url'] = bot.url
    CFG['info']['bot_name'] = bot.full_name
    CFG['info']['bot_username'] = bot.username


async def on_shutdown(dispatcher):

    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    except Exception as err:
        logging.exception(err)
