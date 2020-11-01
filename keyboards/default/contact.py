from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱Поделится контактом📱", request_contact=True)
        ]
    ], resize_keyboard=True
)