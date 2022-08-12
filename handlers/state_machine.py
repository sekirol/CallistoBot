
from aiogram.dispatcher.filters.state import StatesGroup, State

class AppState(StatesGroup):
    initial = State()
    search = State()
