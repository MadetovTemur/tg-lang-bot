# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command
from loader import dp, w, db
from utils.commands.user_command import set_default_commands
from config import COMMANDS, CFG

@dp.message_handler(CommandStart(), state=None)
async def bot_start(msg: types.Message):
  lang = CFG['bot_setting']['defoult']
  await db.add_new_user(msg['from']['id'], msg['from']['username'], lang)
  lang = await db.change_user_lang(msg['from']['id'])
  to_msg = await w.word(lang, 'hello')

  await set_default_commands(dp, COMMANDS)
  await msg.answer(to_msg)




async def is_channel_active(id)->bool:
  chanel = await dp.bot.get_chat_member(CFG['channel']['id'], id)
  if chanel['status'] == 'left':
    return False
  return True


@dp.callback_query_handler(text_contains='subscribed', state=None)
async def edit_bot_lang(callback: types.CallbackQuery) -> None:
  id = callback['from']['id']
  lang = await db.change_user_lang(id)

  if await is_channel_active(id):
    await callback.message.delete()
    to_msg = await w.word(lang, 'subscribed_yes')
    await callback.message.answer(to_msg)
  else:
    to_msg = await w.word(lang, 'subscribed_no')
    await callback.answer(to_msg)