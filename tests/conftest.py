"""
Test fixtures for feedback_bot tests.
"""
import os
import pytest
import pytest_asyncio
import aiosqlite
import app.database.models
from app.config import settings

# Set Test DB PATH
TEST_DB_PATH = "data/test_database.sqlite3"


@pytest_asyncio.fixture(autouse=True)
async def setup_db():
    """Initialize test database before each test and cleanup after."""
    # Force patch the DB_PATH in the settings
    settings.db_path = TEST_DB_PATH
    
    # Remove existing test DB if any
    if os.path.exists(TEST_DB_PATH):
        try:
            os.remove(TEST_DB_PATH)
        except PermissionError:
            pass  # Windows file locking
    
    # Init DB
    await app.database.models.init_db()
    yield
    
    # Cleanup data
    try:
        async with aiosqlite.connect(TEST_DB_PATH) as db:
            await db.execute("DELETE FROM feedbacks")
            await db.commit()
    except Exception:
        pass


@pytest_asyncio.fixture
async def db():
    """Provide async database connection for tests."""
    async with aiosqlite.connect(TEST_DB_PATH) as db:
        yield db

