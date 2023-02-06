from aiogram import Bot, Dispatcher
from aiogram.types import Message
import json

# Подключаем клавиатуру
from core.keyboards.reply import reply_keyboard, local_tell_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import get_inline_keyboard

async def get_list(message:Message, bot:Bot):
    await message.answer('На данный вам доступы следующие карты: \n')


async def get_rules(message:Message, bot:Bot):
    await message.answer('Добро пожаловать в бот для оформления карточек \n' 
                         'вашей задачей будет получение карточек известных российских банков, никаких вложений не потребуется \n'
                         '\n'
                        'Правила просты: вы выбираете нужную вам карту (список будет после создания личного кабинета), затем переходите по'
                         'ссылке в инструкции, далее вам нужно будет заполнить анкету самого банка \n'
                         'В инструкции будут описаны все подробнсти, так что вы всё разберетесь, если возникли вопросы напишите менеджеру @MerciMercurial, вам обязательно помогут'
                        )

async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Здравствуйте {message.from_user.first_name}. Показываем инлайн кнопки',
                         reply_markup=get_inline_keyboard())


# Короче эта библиотека нужна для того, чтобы с текстом работать, преобразовать из текста в объект json

# Тут 3 способа как отправить сообщение юзеру, при это reply цитирует сообщение написавшего
async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}, пройдите, пожалуйста, регистрацию',
                         reply_markup=get_reply_keyboard())
    # await bot.send_message(message.from_user.id, '', reply_markup=get_reply_keyboard())
    # Полключили клавиатуру с помощью атрибута reply_markup



    # await message.answer(f'Привет {message.from_user.first_name}, использовал метод message.answer ')
    # await message.reply(f'Привет {message.from_user.first_name}, использовал метод message.reply')


async def get_help(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           'Возникли проблемы с ботом ? Напишите в поддержку @TechSupportBankBot')



# Эта функция отвечает на текстовый запрос
async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет)')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
    # Тут типа сообщение преобразуется в json
# Если что, после выполнения это функции в консоли будет json объект и его
# можно вставить в json online viewer и посмотреть на атрибуты
