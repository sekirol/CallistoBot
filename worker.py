
from vk_api import VkApi

from tools import get_access_data
from bot_engine import TgBotEngine

def main():
    vk_access = get_access_data("vk")
    vk_session = VkApi(vk_access['login'], vk_access['password'])    
    
    vk_session.auth()
    vk_api = vk_session.get_api()

    bot_engine = TgBotEngine()
    bot_engine.start()

if __name__ == "__main__":
    main()