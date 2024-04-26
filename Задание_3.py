import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

TOKEN = '6578249639:AAECTii6k2H3A0efyc57wcJRbT8Z90A9tDs'
MEMES_DIR = 'MEMES'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def start(message: types.Message):
    await message.reply("Привет! Отправь /meme, чтобы получить случайный мем.")

async def send_meme(message: types.Message):
    meme_files = os.listdir(MEMES_DIR)
    if meme_files:
        meme_path = os.path.join(MEMES_DIR, random.choice(meme_files))
        with open(meme_path, 'rb') as file:
            await bot.send_photo(message.chat.id, file, caption="Вот твой мем!")
    else:
        await message.reply("Извините, мемы закончились.")

async def add_meme(message: types.Message):
    if message.photo:
        photo = message.photo[-1]
        photo_file = await photo.download(destination=MEMES_DIR)
        await message.reply("Спасибо за добавленный мем!")
    else:
        await message.reply("Пожалуйста, отправьте мем в виде фотографии.")


dp.register_message_handler(start, commands=["start"])
dp.register_message_handler(send_meme, commands=["meme"])
dp.register_message_handler(add_meme, content_types=types.ContentType.PHOTO)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
