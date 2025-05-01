from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from config import ADMIN_IDS
from services.rss import fetch_rss
from database import SessionLocal
from models.user import get_or_create_user
from models.feed import FeedSource

async def start_cmd(message: types.Message):
    session = SessionLocal()
    get_or_create_user(session, message.from_user.id, message.from_user.username)
    session.close()
    await message.reply("Welcome to the Feed Aggregator Bot! Type /help for options.")

async def help_cmd(message: types.Message):
    await message.reply("Use /start to subscribe. Admins can use /addfeed, /removefeed, /feeds")

async def get_latest(message: types.Message):
    session = SessionLocal()
    feeds = session.query(FeedSource).all()
    responses = []
    for feed in feeds:
        items = fetch_rss(feed.url)
        if items:
            responses.append(f"\n<b>{feed.url}</b>\n" + "\n".join([f"🔹 {item['title']} - {item['link']}" for item in items[:3]]))
    session.close()
    await message.reply("\n\n".join(responses) if responses else "No feeds available.", parse_mode="HTML")
