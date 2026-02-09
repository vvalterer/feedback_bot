import pytest
from app.database.requests import add_feedback, get_feedbacks
from app.config import settings
import aiosqlite

@pytest.mark.asyncio
async def test_add_and_get_feedback():
    user_id = 12345
    text = "Test feedback unit"
    
    await add_feedback(user_id, text)
    
    feedbacks = await get_feedbacks()
    assert len(feedbacks) > 0
    
    # Check if our feedback is there
    found = False
    for fb in feedbacks:
        if fb[0] == user_id and fb[1] == text:
            found = True
            break
            
    assert found
