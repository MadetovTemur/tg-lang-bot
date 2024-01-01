# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import CFG

async def channel(lang:str):
  btn_minu = InlineKeyboardMarkup(row_width=1)
  if lang.lower() == 'ru':
    btn_minu.add(
      InlineKeyboardButton(text="Канал 1", url=CFG['channel']['url']), # type: ignore
      InlineKeyboardButton(text="Я подписался ✅", callback_data="subscribed"), # type: ignore
    )
    return btn_minu
  elif lang.lower() == 'en':
    btn_minu.add(
      InlineKeyboardButton(text="Channel 1", url=CFG['channel']['url']), # type: ignore
      InlineKeyboardButton(text="I subscribed ✅", callback_data="subscribed"), # type: ignore
    )
    return btn_minu
  else:
    btn_minu.add(
      InlineKeyboardButton(text="Kanal 1", url=CFG['channel']['url']), # type: ignore
      InlineKeyboardButton(text="Obuna boldim ✅", callback_data="subscribed"), # type: ignore
    )
  return btn_minu
