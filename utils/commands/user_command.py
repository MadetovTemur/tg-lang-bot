# -*- coding: utf-8 -*-
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Dispatcher


async def join_command(commands):
  com = []
  for command in commands:
    com.append(
      BotCommand(
        command=command[0],
        description=command[1]
      )
    )
  return com


async def set_default_commands(dp: Dispatcher, command_list):
	command = await join_command(command_list)
	await dp.bot.set_my_commands(commands=command,  scope=BotCommandScopeDefault())
