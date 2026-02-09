"""
Help and start command handlers.
"""
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router(name=__name__)

HELP_TEXT = """
🤖 <b>Feedback Form Bot — Вячеслав Ветошкин</b>

Доступные команды:
/start — запуск
/help — помощь
"""


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Handle /start command."""
    await message.answer(
        "Привет! Я бот Feedback Form под брендом Вячеслав Ветошкин.\n"
        "Напиши /help или просто отправь сообщение."
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help command."""
    await message.answer(HELP_TEXT)
