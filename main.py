from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.utils import executor
import logging

from config import BOT_TOKEN
from bot.dispatcher import dp
from database import init_db

logging.basicConfig(level=logging.INFO)

async def on_startup(dp: Dispatcher):
    init_db()
    await dp.bot.set_my_commands([
        BotCommand("start", "Subscribe to updates"),
        BotCommand("help", "Show help"),
        BotCommand("latest", "Get latest posts"),
        BotCommand("addfeed", "[Admin] Add a new feed"),
        BotCommand("removefeed", "[Admin] Remove a feed"),
        BotCommand("feeds", "[Admin] List all feeds")
    ])
    print("Bot is up and running")

if __name__ == '__main__':
    bot = Bot(token=BOT_TOKEN)
    dp.bot = bot
    executor.start_polling(dp, on_startup=on_startup)
