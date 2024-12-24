from aiogram import Bot, Dispatcher, executor
from bot.config import BOT_TOKEN
from bot.handlers import welcome_handler, question_handler

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрация хэндлеров
dp.register_message_handler(welcome_handler, commands=["start"])
dp.register_message_handler(question_handler)

if __name__ == "__main__":
    executor.start_polling(dp)
