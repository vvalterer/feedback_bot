import pytest
from unittest.mock import AsyncMock, MagicMock
from app.handlers.feature import submit
from aiogram.types import Message, User, Chat

@pytest.mark.asyncio
async def test_submit_handler(mocker):
    # Mock the add_feedback function
    mock_add_feedback = mocker.patch("app.handlers.feature.add_feedback", new_callable=AsyncMock)
    
    # Create a mock message object instead of real frozen Pydantic model
    message = AsyncMock()
    message.text = "Test message"
    message.from_user.id = 123
    message.from_user.full_name = "Test User"
    message.from_user.username = "testuser"
    
    # Call the handler
    await submit(message)
    
    # Assertions
    mock_add_feedback.assert_called_once_with(123, "Test message")
    message.answer.assert_called_once()
