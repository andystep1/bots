from typing import Text
import aiogram

from time import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiohttp.helpers import TOKEN
#from aiogram.methods import SendLocation

from config import TOKEN
from placesapi import find_nearest, get_nearest

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    await message.reply(f'Привет! {user_name}! Нажми на кнопку, чтобы отправить свое местоположение и найти ближайший МакДональдс', reply_markup=get_keyboard())

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton("Найти", request_location=True)
    keyboard.add(button)
    return keyboard

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    loc = (lat, lon)
    aaa = get_nearest(lat, lon)
    reply = find_nearest(loc, aaa)
    reslat = reply[0]
    reslon = reply[1]
    await message.answer('Ближайший Макдональдс находится здесь')
    await message.answer_location(reslat, reslon, reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['locate_me'])
async def cmd_locate_me(message: types.Message):
    reply = "Click on the the button below to share your location"
    await message.answer(reply, reply_markup=get_keyboard(), disable_web_page_preview = False)


#http://www.google.com/maps/search/mcdonalds/@55.7124618,37.5911376,13z/data=!3m1!4b1

if __name__ == '__main__': #всегда тру
    executor.start_polling(dp)