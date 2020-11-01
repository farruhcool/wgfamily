from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

orderdata_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Заказать столик")
        ]
    ], resize_keyboard=True
)
