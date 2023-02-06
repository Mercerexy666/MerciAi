from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
# 1 ReplyKeyboardMarkup нужен для создания клавиатуры
# 2 KeyboardButton нужен для создания кнопки
# 3 KeyboardButtonPollType нужен для создания опросов или викторин
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ряд 1, Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 1, Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 1, Кнопка 3'
        ),
    ],
    [
        KeyboardButton(
            text='Ряд 2, Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 2, Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 2, Кнопка 3'
        ),
        KeyboardButton(
            text='Ряд 2, Кнопка 4'
        ),
    ],
    [
        KeyboardButton(
            text='Ряд 3, Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 3, Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 3, Кнопка 3'
        ),
        KeyboardButton(
            text='Ряд 3, Кнопка 4'
        ),
        KeyboardButton(
            text='Ряд 3, Кнопка 5'
        )
    ]

], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку", seletive=True)
# resize_keyboard - Размер кнопок
# one_time_keyboard - после первого нажатия клавиатура исчеззает
# input_field_placeholder - показывает подсказку в поле ввода значения
# seletive - показывае клавиатуру только тому пользователю кто её запросил

local_tell_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Отправить геолакацию',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text="Отправить контакт",
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text="Создать викторину",
            request_poll=KeyboardButtonPollType()
        #     В скобках можно указать  type='quiz' или type='regular' - первое викторина, вторая опрос с несколькоми ответами
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder="Отправь локацию или номер", seletive=True)

# Второй способ создания клавиатуры

def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Пройти регистрацию')
    keyboard_builder.button(text='Ознакомиться с правилами')
    keyboard_builder.adjust(1, 1)

    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                               input_field_placeholder='Отправь локацию и т.д. я не вижу где это пишется')