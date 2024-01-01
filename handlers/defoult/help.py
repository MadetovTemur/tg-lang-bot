# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import  CommandHelp

from loader import dp



@dp.message_handler(CommandHelp(), state=None)
async def bot_start(msg: types.Message):
  to_msg = f"help"
  await msg.answer(msg)
