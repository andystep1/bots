from typing import Text
import aiogram

from time import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiohttp.helpers import TOKEN

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    print(user_name)
    
    await message.reply(f'Привет! {user_name}! Твой user_id = {user_id}!')

@dp.message_handler() #эхо
async def echo(message: types.Message):
    await message.reply(message.text)

@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    await message.reply(message.text)

@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    #user_name = message.from_user.full_name
    chat_id = message.chat.id
    await bot.send_photo(chat_id, 'https://sun9-74.userapi.com/impg/iEa6AJ2_XN_FbOvEM7yioWaHg2YR3-U-U_E3pw/jh0iclB4ED8.jpg?size=1280x1201&quality=95&sign=e684a11b1faeaa24a33e210339152f16&type=album')
if __name__ == '__main__': #всегда тру
    executor.start_polling(dp)