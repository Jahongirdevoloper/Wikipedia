from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
storege = MemoryStorage()

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot, storage=storege)

# be853f0f2345cbd4785fbf31