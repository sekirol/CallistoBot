
from vk_api import VkApi

from .tools import get_access_data

VK_CONFIG_PATH = "./app/data/vk_config.v2.json"

class VkSession():
    def __init__(self):
        self._connect()

    def _connect(self):
        access = get_access_data("vk")
        session = VkApi(access['login'], access['password'], config_filename=VK_CONFIG_PATH)
    
        session.auth()
        self.api = session.get_api()

    def get_user_data(self):
        return self.api.users.get()