from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook Air 13 M1 2020',
                            callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='Macbook Pro 14 M1 2021',
                            callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='Apple Macbook Pro 16 2019',
                            callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))
    keyboard_builder.button(text='bappea', url='https://t.me/bappea')
    keyboard_builder.button(text='Merci', url='https://t.me/MerciMercurial')

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()

# # Почему-то не сработал этот код, связано наверное с версией или хз, но энивей мне этот способ нравится больше
# select_macbook = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Macbook Air 13 M1 2020',
#             calback_data='apple_air_13_m1_2020'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Macbook Pro 16 M1 2019',
#             calback_data='apple_pro_16_i7_2019'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='Macbook Air 13 M1 2020',
#             calback_data='apple_air_13_m1_2020'
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='31231'
#
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text='123'
#         )
#     ]
# ])
