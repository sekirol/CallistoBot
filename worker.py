
import logging

from bot_engine import TgBotEngine
from vk_session import VkSession

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )    
    logger.info("Starting bot")

    vk_session = VkSession()

    bot_engine = TgBotEngine()
    bot_engine.start()

if __name__ == "__main__":
    main()