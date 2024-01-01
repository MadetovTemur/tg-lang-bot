# -*- coding: utf-8 -*-

from typing import Callable, Awaitable, Dict, Any
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
import logging

from loader import dp, db
from keyboards.inlayins.subscrib import channel, CFG

class ChanelMiddleware(BaseMiddleware):

    async def is_channel_active(self, id)->bool:
      chanel = await dp.bot.get_chat_member(CFG['channel']['id'], id)
      if chanel['status'] == 'left':
        return False
      return True

    # В просесе
    async def on_process_message(self, msg: types.Message, data:dict):
      id = msg['from']['id']
      lang = msg['from']['language_code']
      if not await self.is_channel_active(id):
        await msg.answer('Kanalga patpis bosing ', reply_markup=await channel(lang))
        raise CancelHandler()




    async def on_process_callback_query(self, callback: types.CallbackQuery, data:dict):
      id = callback['from']['id']
      if not await self.is_channel_active(id) and callback.data != 'subscribed':
        lang = msg['from']['language_code']
        await callback.message.answer('Kanalga patpis bosing ', reply_markup=await channel(lang))
        raise CancelHandler()







