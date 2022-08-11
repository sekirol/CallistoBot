
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.files import JSONStorage

from tools import get_access_data

FSM_STORAGE_PATH = "app_state.json"

def main():
    bot = Bot(get_access_data("telegram"))

    storage = JSONStorage(FSM_STORAGE_PATH)
    dp = Dispatcher(bot, storage=storage)

    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()