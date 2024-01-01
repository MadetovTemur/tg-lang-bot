# -*- coding: utf-8 -*-
from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .defoult import DefoultMiddlewares
from .channel import ChanelMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ChanelMiddleware())
    dp.middleware.setup(DefoultMiddlewares())
