from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from fluent.runtime import FluentLocalization


async def set_bot_commands(bot: Bot, l10n: FluentLocalization):
    await bot.set_my_commands(
        [
            BotCommand(command="start", description=l10n.format_value("menu-start")),
            BotCommand(command="spin", description=l10n.format_value("menu-spin")),
            BotCommand(command="stop", description=l10n.format_value("menu-stop")),
            BotCommand(command="help", description=l10n.format_value("menu-help")),
            BotCommand(command="spin_settings", description=l10n.format_value("menu-spin-settings")),
        ],
        scope=BotCommandScopeDefault()
    )
