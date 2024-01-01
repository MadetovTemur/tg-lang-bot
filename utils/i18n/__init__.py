# -*- coding: utf-8 -*-

class WordBase:

  def __init__(self, words):
    self.uz = words['uz']
    self.ru = words['ru']
    self.en = words['en']


  async def word(self, lang:str, prefkis:str)-> str:
    if lang.lower() == 'ru':
      return self.ru[prefkis]
    elif lang.lower() == 'uz':
      return self.uz[prefkis]
    elif lang.lower() == 'en':
      return self.en[prefkis]
    else:
      return 'View not fount'