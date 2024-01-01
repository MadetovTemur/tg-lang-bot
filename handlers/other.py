# -*- coding: utf-8 -*-
from aiogram import types
from loader import dp


@dp.message_handler(state=None)
async def bot_help(msg: types.Message):
  # await dp.bot.send_message(cfg['chanel']['id'], msg.text)
  await msg.reply(msg) # type: ignore


#/*
# Dubaynig  70-yilda rivojlandi. menga esa butun umrim xam etmaydi
# */