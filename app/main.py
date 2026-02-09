"""
Feedback Form Bot - Entry Point.
"""
import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import feature, help_text
from app.database.models import init_db
from app.config import settings

# Configure logging
logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)


async def main():
    """Initialize bot and start polling."""
    await init_db()

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    dp.include_routers(feature.router, help_text.router)

    logger.info("Bot started!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
