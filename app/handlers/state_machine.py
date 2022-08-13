
from aiogram.dispatcher.filters.state import StatesGroup, State

from datetime import datetime, timedelta

INACTIVE_SESSION_MAX_DURATION = 5

class AppState(StatesGroup):
    initial = State()
    search = State()

class CurrentSession:
    def __init__(self):
        self.update_activity_time()

    def __str__(self):
        session_duration = (datetime.now() - self._last_activity_time)
        return f"Session lasts {session_duration.seconds} second. " \
               f"Session is {'active' if self.is_session_active() else 'inactive'}."

    def update_activity_time(self):
        self._last_activity_time = datetime.now()

    def is_session_active(self) -> bool:
        session_duration = datetime.now() - self._last_activity_time
        return session_duration < timedelta(minutes=INACTIVE_SESSION_MAX_DURATION)
