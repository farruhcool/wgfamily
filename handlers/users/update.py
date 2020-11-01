from aiogram import types
from aiogram.dispatcher.filters import Command
from utils.db_api import db_commands as commands

from loader import dp


@dp.message_handler(Command("upgrade"))
async def send_info_upgrade(message: types.Message):
    admin = message.from_user.id
    all_users = await commands.get_users_id()
    if admin == 81039470:
        for i in all_users:
            await dp.bot.send_message(i,
                                      f"This bot has a new version! Please type /start to upgrade your version")
    else:
        await message.answer(f"You have not permission to use this command")