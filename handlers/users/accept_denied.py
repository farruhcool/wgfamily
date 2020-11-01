from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from loader import dp

@dp.message_handler(text = "Принять")
async def accept(message: types.Message, state: FSMContext):
    await dp.bot.send_message(81039470, "Ваш заказ был принят",reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text = "Отказать")
async def accept(message: types.Message):
    await dp.bot.send_message(81039470, "Ваш заказ не был принят", reply_markup=ReplyKeyboardRemove())