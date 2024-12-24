from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext

# Хэндлер приветствия
async def welcome_handler(message: types.Message):
    await message.answer("Добро пожаловать! Чем я могу помочь?")

# Хэндлер обработки простых вопросов
async def question_handler(message: types.Message):
    # Логика для автоматических ответов
    if "цена" in message.text.lower():
        await message.answer("Стоимость услуги составляет 1000 рублей.")
    else:
        await message.answer("Спасибо за ваш вопрос. Мы ответим вам в ближайшее время.")
