from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

flags = {"throttling_key": "spin_settings"}
router = Router()

@router.message(Command("spin_settings"))
async def spin_settings(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Number of Spins", callback_data="set_spins")
    builder.button(text="SOLSSPIN per Spin", callback_data="set_solsspin")
    await message.answer("Choose a setting to adjust:", reply_markup=builder.as_markup())

@router.callback_query(F.data.in_(["set_spins", "set_solsspin"]))
async def button_callback(query: CallbackQuery):
    await query.answer()
    if query.data == "set_spins":
        await query.message.answer("Enter the number of spins (1-5):")
        query.bot.spin_settings = 'spins'
    elif query.data == "set_solsspin":
        await query.message.answer("Enter the amount of SOLSSPIN per spin (1-100):")
        query.bot.spin_settings = 'solsspin'

@router.message(F.text)
async def handle_setting(message: Message):
    if not hasattr(message.bot, 'spin_settings'):
        return

    setting = message.bot.spin_settings
    value = message.text

    if setting == 'spins':
        try:
            spins = int(value)
            if 1 <= spins <= 5:
                message.bot.spins = spins
                await message.answer(f"Number of spins set to {spins}")
            else:
                await message.answer("Please enter a number between 1 and 5")
        except ValueError:
            await message.answer("Please enter a valid number")
    elif setting == 'solsspin':
        try:
            solsspin = int(value)
            if 1 <= solsspin <= 100:
                message.bot.solsspin = solsspin
                await message.answer(f"SOLSSPIN per spin set to {solsspin}")
            else:
                await message.answer("Please enter a number between 1 and 100")
        except ValueError:
            await message.answer("Please enter a valid number")

    message.bot.spin_settings = None
