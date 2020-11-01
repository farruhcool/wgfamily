from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

typeofevent_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="День рождение")
        ],
        [
            KeyboardButton(text="Свадьба")
        ],
        [
            KeyboardButton(text="Посиделки")
        ],
        [
            KeyboardButton(text="Другое")
        ]
    ], resize_keyboard=True
)
amount_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1")
        ],
        [
            KeyboardButton(text="2")
        ],
        [
            KeyboardButton(text="3")
        ],
        [
            KeyboardButton(text="4")
        ],
        [
            KeyboardButton(text="5")
        ],
        [
            KeyboardButton(text="Более 5 человек")
        ],
    ]
)
type_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Семья")
        ],
        [
            KeyboardButton(text="Друзья")
        ],
        [
            KeyboardButton(text="Гости")
        ],
[
            KeyboardButton(text="Другое")
        ]
    ]
)
time_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="с 09:00 до 12:00")
        ],
        [
            KeyboardButton(text="с 12:00 до 15:00")
        ],
        [
            KeyboardButton(text="с 15:00 до 18:00")
        ],
        [
            KeyboardButton(text="с 18:00 до 21:00")
        ]
    ]
)