
from vk_api import VkApi

from tools import get_access_data

class VkSession():
    def __init__(self):
        self._connect()

    def _connect(self):
        access = get_access_data("vk")
        session = VkApi(access['login'], access['password'])
    
        session.auth()
        self.api = session.get_api()

    def get_user_data(self):
        return self.api.users.get()