
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.files import JSONStorage

from vk_api import VkApi

from tools import get_access_data

FSM_STORAGE_PATH = "app_state.json"

def main():
    vk_access = get_access_data("vk")
    vk_session = VkApi(vk_access['login'], vk_access['password'])    
    
    vk_session.auth()
    vk_api = vk_session.get_api()

    tg_bot = Bot(get_access_data("telegram"))

    storage = JSONStorage(FSM_STORAGE_PATH)
    dp = Dispatcher(tg_bot, storage=storage)

    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()