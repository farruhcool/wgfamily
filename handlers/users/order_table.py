from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.confirm_button import confirm_keyboard
from keyboards.default.typeofevent_button import typeofevent_keyboard, amount_keyboard, type_keyboard, time_keyboard
from loader import dp
from states import OrderState


@dp.message_handler(text="Заказать столик")
async def enter_orderstate(message: types.Message):
    await message.answer("Введите на какую дату вы хотите забронировать место\n"
                         "Пример(День.Месяц.Год): 10.10.2020", reply_markup=ReplyKeyboardRemove())
    await OrderState.Question1.set()

@dp.message_handler(state=OrderState.Question1)
async def answer_question1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("На какое время вы хотите забронировать место", reply_markup=time_keyboard)

    await OrderState.Question2.set()

@dp.message_handler(state=OrderState.Question2)
async def answer_question2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer2=answer)

    await message.answer("Из какой компании состоит ваш коллектив?", reply_markup=type_keyboard)

    await OrderState.Question3.set()

@dp.message_handler(state=OrderState.Question3)
async def answer_question3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer3=answer)

    await message.answer("Из скольких человек состоит ваш коллектив?", reply_markup=amount_keyboard)

    await OrderState.Question4.set()

@dp.message_handler(state=OrderState.Question4)
async def answer_question4(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer4 = answer)

    await message.answer("Какое мероприятие вы отмечаете?",reply_markup=typeofevent_keyboard)

    await OrderState.Question5.set()
@dp.message_handler(state=OrderState.Question5)
async def answer_question5(message: types.Message, state: FSMContext):
    customer_id = message.from_user.id
    answer = message.text
    await state.update_data(answer5=answer)

    data = await state.get_data()

    date = data.get("answer1")
    time = data.get("answer2")
    type = data.get("answer3")
    amount = data.get("answer4")
    typeofevent = data.get("answer5")

    await message.answer(f"Дата мероприятия: {date}\n"
    f"Время мероприятия: {time}\n"
    f"Для кого организовывается мероприятие: {type}\n"
    f"Из скольких человек состоит ваш коллектив: {amount}\n"
    f"Тип мероприятия: {typeofevent}\n", reply_markup=confirm_keyboard)

    await state.reset_state(with_data=False)
