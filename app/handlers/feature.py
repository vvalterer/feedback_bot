import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.enums import ParseMode
from app.database.requests import add_feedback
from app.config import settings

router = Router(name=__name__)
logger = logging.getLogger(__name__)


@router.message()
async def submit(m: Message):
    """Handle all text messages as feedback submissions."""
    try:
        # Save to Database
        await add_feedback(m.from_user.id, m.text)
        await m.answer("✅ Заявка принята! Администратор свяжется с вами.")
        
        # Notify Admins
        for admin_id in settings.admin_ids:
            try:
                await m.bot.send_message(
                    chat_id=admin_id,
                    text=f"📩 <b>Новая заявка!</b>\n\n👤: {m.from_user.full_name} (@{m.from_user.username})\n💬: {m.text}",
                    parse_mode=ParseMode.HTML
                )
            except Exception as e:
                logger.error(f"Failed to send to admin {admin_id}: {e}")
                
    except Exception as e:
        logger.error(f"Error processing feedback: {e}")
        await m.answer("❌ Произошла ошибка при сохранении заявки.")
