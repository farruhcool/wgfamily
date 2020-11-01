from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hcode, hbold

from keyboards.default.contact import contact_keyboard
from keyboards.default.orderdata import orderdata_keyboard
from utils.db_api import db_commands as commands
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    user = await commands.add_user(user_id=message.from_user.id, full_name=message.from_user.full_name,
                                   username=message.from_user.username)
    count = await commands.count_users()
    new_user = await commands.select_user(user_id=message.from_user.id)
    await dp.bot.send_message(81039470,
                              hcode(f"Зарегистрирован новый ползователь!\n"
                                    f"ID: {new_user.user_id}\n"
                                    f"Name: {new_user.name}\n"
                                    f"Username: {new_user.username}"))
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}',
                f'Вы были занесены в базу',
                f'В базе <b>{count}</b> пользователей',
            ]))
    await message.answer(hbold(f'Для продолжения работы поделитесь вашим номеров'), reply_markup=contact_keyboard)
    await state.set_state("tel")


@dp.message_handler(state="tel", content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message, state: FSMContext):
    # id = message.from_user.id
    user_phone = message.contact
    tel = await commands.update_user_tel(id=message.from_user.id, tel=user_phone.phone_number)
    usero = await commands.select_user(user_id=message.from_user.id)
    await message.answer(f"Спасибо! Номер телефона записан в БД \n", reply_markup=ReplyKeyboardRemove())
    await dp.bot.send_message(81039470, "В базу добавлен новый номер телефона: \n" +
                              hcode(f"id={usero.user_id}\n"
                                    f"name={usero.name}\n"
                                    f"tel={tel.tel}\n"))
    await state.finish()

    await message.answer(text="Для того чтобы забронировать место нажмите на кнопку приведенную ниже",
                         reply_markup=orderdata_keyboard)



#