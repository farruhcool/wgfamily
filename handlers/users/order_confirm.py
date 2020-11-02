from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.orderdata import orderdata_keyboard
from utils.db_api import db_commands as commands
from loader import dp


@dp.message_handler(text="Подтвердить")
async def order_confirm(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    order_data = await commands.select_user(user_id=user_id)
    data = await state.get_data()
    customer_id = message.from_user.id
    date = data.get("answer1")
    time = data.get("answer2")
    type = data.get("answer3")
    amount = data.get("answer4")
    typeofevent = data.get("answer5")

    dbwrite = await commands.add_order(customer_id=customer_id, date=date, time=time, type=type, amount=amount,
                                       typeofevent=typeofevent)

    await dp.bot.send_message(-1001321174064,f"id: {order_data.user_id}\n"
                              f"Имя заказчика: {order_data.name}\n"
                              f"Никнэйм заказчика: @{order_data.username}\n"
                              f"Телефонный номер заказчика: +{order_data.tel}\n"
                              f"Дата мероприятия: {date}\n"
                              f"Время мероприятия: {time}\n"
                              f"Для кого организовывается мероприятие: {type}\n"
                              f"Из скольких человек состоит кампания: {amount}\n"
                              f"Тип мероприятия: {typeofevent}\n")
    await message.answer("Ваш заказ был передан на обработку, в скором времени наш менеджер свяжется с вами",
                         reply_markup=orderdata_keyboard)

@dp.message_handler(text="Отмена")
async def cancel_func(message: types.Message):
    await message.answer("Отменено", reply_markup=orderdata_keyboard)