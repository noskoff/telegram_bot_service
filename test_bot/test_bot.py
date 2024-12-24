from aiogram.types import Message
from bot.handlers import question_handler

class MockBot:
    async def answer(self, text):
        return text

async def test_question_handler():
    mock_message = Message(text="Какая цена?")
    mock_bot = MockBot()
    response = await question_handler(mock_message)
    assert response == "Стоимость услуги составляет 1000 рублей."
