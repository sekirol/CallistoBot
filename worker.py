
import logging

from app.bot_engine import TgBotEngine

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )    
    logger.info("Starting bot")

    bot_engine = TgBotEngine()
    bot_engine.start()

if __name__ == "__main__":
    main()