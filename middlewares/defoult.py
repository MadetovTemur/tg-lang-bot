# -*- coding: utf-8 -*-

from typing import Callable, Awaitable, Dict, Any
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
import logging

from loader import dp, db

class DefoultMiddlewares(BaseMiddleware):

    # В просесе
    async def on_process_message(self, msg: types.Message, data:dict):
      try:
        await dp.bot.send_chat_action(msg.chat.id, action=types.ChatActions.TYPING)
        await db.oldtime(msg.chat.id)
      except Exception as err:
        logging.exception(err)


    async def on_process_callback_query(self, callback: types.CallbackQuery, data:dict):
      try:
        await dp.bot.send_chat_action(callback.message.chat.id, action=types.ChatActions.TYPING)
        await db.oldtime(callback['from']['id'])
      except Exception as err:
        logging.exception(err)