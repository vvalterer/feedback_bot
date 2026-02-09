import aiosqlite
from app.config import settings

async def add_feedback(user_id: int, text: str):
    async with aiosqlite.connect(settings.db_path) as db:
        await db.execute(
            "INSERT INTO feedbacks (user_id, text) VALUES (?, ?)",
            (user_id, text)
        )
        await db.commit()

async def get_feedbacks():
    async with aiosqlite.connect(settings.db_path) as db:
        async with db.execute("SELECT user_id, text, created_at FROM feedbacks ORDER BY created_at DESC") as cursor:
            return await cursor.fetchall()
