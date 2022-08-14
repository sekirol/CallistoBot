
from aiogram.dispatcher.filters.state import StatesGroup, State
from datetime import datetime, timedelta

INACTIVE_SESSION_MAX_DURATION = 5

class AppState(StatesGroup):
    initial = State()
    search = State()

class StateContext:
    def __init__(self):
        self._last_activity_time = None

        self.update_activity_time()

    def get_last_activity(self) -> str:
        return self._last_activity_time.isoformat(sep=" ", timespec="seconds")

    def update_activity_time(self):
        self._last_activity_time = datetime.now()

    def is_state_active(self) -> bool:
        session_duration = datetime.now() - self._last_activity_time
        return session_duration < timedelta(minutes=INACTIVE_SESSION_MAX_DURATION)
