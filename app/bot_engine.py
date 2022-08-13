
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.files import JSONStorage

from .handlers.common import register_handlers_common
from .handlers.search import register_handlers_search
from .tools import get_access_data

FSM_STORAGE_PATH = "app_state.json"

async def shutdown(dp: Dispatcher):
    await dp.storage.close()

class TgBotEngine:
    def __init__(self):
        bot = Bot(get_access_data("telegram"))
        storage = JSONStorage(FSM_STORAGE_PATH)
        
        self.dp = Dispatcher(bot, storage=storage)

        self._init_handlers()

    def _init_handlers(self):
        register_handlers_common(self.dp)
        register_handlers_search(self.dp)

    def start(self):
        executor.start_polling(self.dp, skip_updates=True, on_shutdown=shutdown)

