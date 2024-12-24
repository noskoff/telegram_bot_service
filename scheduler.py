from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

async def send_message(bot: Bot, chat_id: int, text: str):
    await bot.send_message(chat_id, text)

def run_scheduler(bot: Bot, admin_id: int):
    # Рассылка каждое утро в 9:00
    scheduler.add_job(send_message, "cron", hour=9, minute=0,
                      args=[bot, admin_id, "Доброе утро! Специальные предложения сегодня: ..."])
    scheduler.start()
