from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
import asyncio
import logging

# Не забывай импортировать из handlerов
from core.handlers.basic import get_start, get_hello, get_help, get_rules
from core.settings import settings

from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_false_contact

from aiogram.filters import ContentTypesFilter, Command, CommandStart
from aiogram import F

from core.utils.commands import set_commands
from core.handlers.basic import get_inline
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check



# Библиотеки и основная работа расписана в pay.py

# Добавиль фильтры ContentTypesFilter который помогает видеть фото или видео и многое другое
# CommandStart специальный фильтр предназначеный для /start
# Пиздец, я мог сразу использовать F, нахуй этот откат был нужен, блять пиздец

# Не забывай, что для функций нужно писать async, а для самих операций await


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот выключен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s - "
                        )
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    # Регистрировать мидлвари, нужно раньше, чем прочие хендлеры

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, ContentTypesFilter(content_types=[ContentType.SUCCESSFUL_PAYMENT]))
    dp.shipping_query.register(shipping_check)

    # dp.message.register(get_inline, Command(commands='knopki'))
    dp.callback_query.register(select_macbook, MacInfo.filter())
    # Можно добавить филльтр F.model == 'pro'
    # dp.message.register(get_locationg, ContentTypesFilter(content_types=[ContentType.LOCATION]))
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_help, Command(commands='help'))
    dp.message.register(get_rules, F.text == 'Ознакомиться с правилами')
    # dp.message.register(get_cansel, Command(commands='cancel'))
    # dp.message.register(get_nudes, Command(commands='nudes'))
    # Добавил фильтр Command, чтобы хендлер dp.message.register срабатывал, когда нажимаются команды /start или ран

    # dp.message.register(get_photo, ContentTypesFilter(content_types=[ContentType.PHOTO]))
    dp.message.register(get_hello, (F.text == 'Привет') | (F.text == 'привет') | (F.text == 'ПРИВЕТ'))
    # Благодаря Софе лучше понял как работают фильтры, использовал логический
    # Тут прописываем через F фильтр код-слово, в данном случае привет
    # dp.message.register(get_photo, F.photo)
    # ЭТО ПИЗДЕЦ. Я МОГ ИЗНАЧАЛЬНО ИСПОЛЬЗОВАТЬ F ВМЕСТО ТОГО ЧТОБЫ ЕБАТЬСЯ С ВЕРХНЕЙ СТРОКОЙ. ЕЩЁ ОТКАТ ДЕЛАЛ ВЕРСИИ
    # get start пишем без скобки, потому-что не вызываем функцию, а просто передаем ей название
    # dp.message.register(get_start, CommandStart())

    dp.message.register(get_true_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]), IsTrueContact())
    dp.message.register(get_false_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]))
    # С этими хендлерами всё сложно, но я запомнил одно, что хендлеры обрабатываются поочередно
    # Сначала верхний потом нижний

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
