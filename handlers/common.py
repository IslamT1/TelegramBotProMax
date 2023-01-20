from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

# Этот хэндлер срабатывает на команду /start
async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(LEXICON_RU['/start'], reply_markup=types.ReplyKeyboardRemove())

# Этот хэндлер срабатывает на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

# Этот хэндлер срабатывает на команду /cancel
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Отменено", reply_markup=types.ReplyKeyboardRemove())


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
