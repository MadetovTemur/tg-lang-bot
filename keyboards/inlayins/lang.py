# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from emoji import emojize


async def langs(lang:str):
  btn_minu = InlineKeyboardMarkup(row_width=1)
  if lang.lower() == 'ru':
    btn_minu.add(
      InlineKeyboardButton(text="Ru ✅", callback_data="lang:ru"), # type: ignore
      InlineKeyboardButton(text="Uz ", callback_data="lang:uz"), # type: ignore
      InlineKeyboardButton(text="En ", callback_data="lang:en"), # type: ignore
    )
    return btn_minu
  elif lang.lower() == 'en':
    btn_minu.add(
      InlineKeyboardButton(text="Ru ", callback_data="lang:ru"), # type: ignore
      InlineKeyboardButton(text="Uz ", callback_data="lang:uz"), # type: ignore
      InlineKeyboardButton(text="En ✅", callback_data="lang:en"), # type: ignore
    )
    return btn_minu
  else:
    btn_minu.add(
      InlineKeyboardButton(text="Ru ", callback_data="lang:ru"), # type: ignore
      InlineKeyboardButton(text="Uz ✅", callback_data="lang:uz"), # type: ignore
      InlineKeyboardButton(text="En ", callback_data="lang:en"), # type: ignore
    )
  return btn_minu



# cancel = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
#   [
#     InlineKeyboardMarkup(text=emojize(':right_arrow_curving_left:'), callback_data="minu:cancel")
#   ]
# ])






# btn_minu_admin = InlineKeyboardMarkup(row_width=2).add(
#     InlineKeyboardButton(text=f"Сена UC {emojize(':bar_chart:')}", callback_data="minu:price"), # type: ignore
#     InlineKeyboardButton(text=f"Заказать UC {emojize(':recycling_symbol:')}", callback_data="minu:add_new_order"), # type: ignore
#   ).add(
#     InlineKeyboardButton(text=f"Ваш заказиы. {emojize(':abacus:')}", callback_data="minu:orders"), # type: ignore
#     InlineKeyboardButton(text=f"Biz xaqimizda {emojize(':busts_in_silhouette:')}",  callback_data="minu:bot") # type: ignore
#   ).add(
#     InlineKeyboardButton(text=f"Ваш Пользователь. {emojize(':performing_arts:')}", callback_data="minu:users"), # type: ignore
#     InlineKeyboardButton(text=f"Изменить сена UC {emojize(':writing_hand:')}",  callback_data="minu:edit_price") # type: ignore
#   )




# def echo_btns(produc_id, id):
#   btns = InlineKeyboardMarkup(row_width=1).add(
#     InlineKeyboardButton(text=f"Оплачень {emojize(':check_mark_button:')}", callback_data=f'order:{produc_id}:true:{id}'), # type: ignore
#     InlineKeyboardButton(text=f"Не правилние id {emojize(':memo:')}", callback_data=f'order:{produc_id}:No id:{id}'), # type: ignore
#     InlineKeyboardButton(text=f"Не перевель деньги {emojize(':money_with_wings:')}", callback_data=f'order:{produc_id}:No maney:{id}') # type: ignore
#   )
#   return btns