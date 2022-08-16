
from aiogram.dispatcher.filters.state import StatesGroup, State

INACTIVE_SESSION_MAX_DURATION = 5

class AppState(StatesGroup):
    initial = State()
    search = State()
