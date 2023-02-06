# Здесь будут записаны команды для бота
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


# command - название, description - описание

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
