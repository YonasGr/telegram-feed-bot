from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .handlers import register_handlers

dp = Dispatcher(storage=MemoryStorage())
register_handlers(dp)
