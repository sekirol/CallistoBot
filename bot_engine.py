
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.files import JSONStorage

from tools import get_access_data

FSM_STORAGE_PATH = "app_state.json"

class TgBotEngine:
    def __init__(self):
        bot = Bot(get_access_data("telegram"))
        storage = JSONStorage(FSM_STORAGE_PATH)
        
        self.dp = Dispatcher(bot, storage=storage)


    def start(self):
        executor.start_polling(self.dp, skip_updates=True, on_shutdown=self._shutdown)

    def _init_handlers(self):
        pass

    async def _shutdown(self):
        await self.dp.storage.close()
