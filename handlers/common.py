from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU


# Этот хэндлер срабатывает на команду /start
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(LEXICON_RU['/start'], reply_markup=types.ReplyKeyboardRemove())


# Этот хэндлер срабатывает на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


# Этот хэндлер срабатывает на команду /cancel
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Состояние сброшено", reply_markup=types.ReplyKeyboardRemove())


def register_handlers_common(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))  # , state="*")
    dp.message.register(process_help_command, Command('help'))
    dp.message.register(cmd_cancel, Command("stop"))  # , state="*")
    dp.message.register(cmd_cancel, F.text.lower() == "стоп")  # , state="*")
