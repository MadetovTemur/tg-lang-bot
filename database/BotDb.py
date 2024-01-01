# -*- coding: utf-8 -*-
import sqlite3, asyncio, time, logging
from datetime import datetime
from .tables import (users, quotes, admins)

class DBase:

  def __init__(self, db_file:str):
    self.connection = sqlite3.connect(db_file)
    self.cursor = self.connection.cursor()
    self.now = datetime.now().strftime("%d-%m-%Y|%H:%M:%S")
    logging.debug('DataBaze __connection__ OK !!')


  async def create_tables(self):
    try:
      with self.connection:
        self.cursor.execute(users)
        self.cursor.execute(quotes)
        self.cursor.execute(admins)
      return True
    except Exception as err:
      return False

  async	def serch_user_id_bool(self, id:int) -> bool:
    with self.connection:
      data = self.cursor.execute(f"SELECT * FROM `users` WHERE `user_id` = {id}").fetchall()
    return bool(len(data))

  async def add_new_user(self, user_id:int, username:str, chat_lang:str):
    try:
      if await self.serch_user_id_bool(user_id):
        return False

      query = f"""INSERT INTO `users` (`user_id`, `username`, `startime`, `chat_lang`, `oldtime`)
        VALUES ({user_id}, '{username}', '{self.now}', '{chat_lang}', '{self.now}')"""
      with self.connection:
        self.cursor.execute(query)
    except Exception as err:
      logging.exception(err)

  async def oldtime(self, user_id):
    try:
      if await self.serch_user_id_bool(user_id):
        query = "UPDATE `users` SET `oldtime` = ?  WHERE `user_id` = ? "
        with self.connection:
          self.cursor.execute(query, (self.now, user_id))
    except Exception as err:
      logging.exception(err)

  async def change_user_lang(self, user_id):
    try:
      if not await self.serch_user_id_bool(user_id):
        return 'ru'
      with self.connection:
        data = self.cursor.execute(f"SELECT `chat_lang` FROM `users` WHERE `user_id` = {user_id}")
      return data.fetchone()[0]
    except Exception as err:
      logging.exception(err)

  async def edit_user_lang(self, user_id, lang):
    try:
      if await self.serch_user_id_bool(user_id):
        query = "UPDATE `users` SET `chat_lang` = ?  WHERE `user_id` = ? "
        with self.connection:
          self.cursor.execute(query, (lang, user_id))
    except Exception as err:
      logging.exception(err)
