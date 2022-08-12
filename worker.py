
from bot_engine import TgBotEngine
from vk_session import VkSession

def main():
    vk_session = VkSession()

    bot_engine = TgBotEngine()
    bot_engine.start()

if __name__ == "__main__":
    main()