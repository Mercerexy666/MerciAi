# Тут написаны хендлеры для работы с кастомным фильтром iscontact

from aiogram.types import Message
from aiogram import Bot

# 1яя версия кода
# async def get_true_contact(message: Message, bot: Bot):
#     await message.answer('Ты отправил свой контакт')

# 2ая версия кода
async def get_true_contact(message: Message, bot: Bot, phone:str):
    await message.answer(f'Ты отправил свой контакт {phone}')


async def get_false_contact(message: Message, bot: Bot):
    await message.answer('Ты отправил НЕ свой контакт')
