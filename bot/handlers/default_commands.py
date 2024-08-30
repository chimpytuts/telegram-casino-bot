from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from fluent.runtime import FluentLocalization

from bot.config_reader import Settings
from bot.keyboards import get_spin_keyboard

flags = {"throttling_key": "default"}
router = Router()


@router.message(Command("start", "help"))
async def cmd_start(message: types.Message, l10n: FluentLocalization):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/start")],
            [KeyboardButton(text="/spin")],
            [KeyboardButton(text="/stop")],
            [KeyboardButton(text="/help")],
            [KeyboardButton(text="/spin_settings")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        l10n.format_value("start-text"),
        reply_markup=keyboard
    )


@router.message(Command("stop"), flags=flags)
async def cmd_stop(message: Message, l10n: FluentLocalization):
    await message.answer(
        l10n.format_value("stop-text"),
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command("help"), flags=flags)
async def help_command(message: Message, l10n: FluentLocalization):
    help_text = l10n.format_value("help-text") + "\n/settings - Adjust spin settings"
    await message.answer(help_text)
