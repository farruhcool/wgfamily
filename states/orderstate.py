from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderState(StatesGroup):
    Question1 = State()
    Question2 = State()
    Question3 = State()
    Question4 = State()
    Question5 = State()