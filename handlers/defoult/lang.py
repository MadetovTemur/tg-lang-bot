# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command
from loader import dp, w, db
from keyboards.inlayins.lang import langs


@dp.message_handler(Command('edit_bot_lang'), state=None)
async def bot_lang(msg: types.Message):
  lang = await db.change_user_lang(msg['from']['id'])
  to_msg = ('Bot sozlasha oladigan tildan birsin tanlang!\n'\
            '' )

  lang_minu = await langs(lang)
  await msg.answer(to_msg, reply_markup=lang_minu)

async def is_lang(data)->str:
  if data == 'lang:ru':
    return 'ru'
  elif data == 'lang:en':
    return 'en'
  else:
    return 'uz'

@dp.callback_query_handler(text_contains='lang', state=None)
async def edit_bot_lang(callback: types.CallbackQuery) -> None:
  lang = await is_lang(callback.data)
  await db.edit_user_lang(callback['from']['id'], lang)
  await callback.message.delete()
  to_msg = await w.word(lang, 'edit_bot_lang')
  await callback.message.answer(to_msg)
