# -*- coding: utf-8 -*-
# Импорт пакетий
import logging, asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Импорт файли
from config import CFG, WORDS
from utils.i18n import WordBase
from database import DBase


try:
  w = WordBase(WORDS)
  loop = asyncio.new_event_loop()
  bot = Bot(token=CFG['bot_setting']['token'], parse_mode=types.ParseMode.HTML, protect_content=CFG['bot_setting']['protect_content'])
  storage = MemoryStorage()
  dp = Dispatcher(bot, storage=storage, loop=loop)

  db = DBase('data/TelegramDB.db')
except Exception as err:
  logging.exception(err)
