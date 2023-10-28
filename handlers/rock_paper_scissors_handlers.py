from aiogram import Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
# from aiogram.types.message import Text
from aiogram.fsm.state import State, StatesGroup

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import yes_no_kb, game_kb
from services.services import get_bot_choice, get_winner


class RockPaperFSM(StatesGroup):
    # Состояния
    processing_rock_paper = State()


# Этот хэндлер срабатывает на команду /rock_paper_scissors
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/rock_paper_scissors'], reply_markup=yes_no_kb)
    await RockPaperFSM.processing_rock_paper.set()


# Этот хэндлер срабатывает на согласие пользователя играть в игру
async def process_yes_answer(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


# Этот хэндлер срабатывает на отказ пользователя играть в игру
async def process_no_answer(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['no'], reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


# Этот хэндлер срабатывает на любую из игровых кнопок
async def process_game_button(message: Message, state: FSMContext):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.message.register(process_start_command, Command('rock_paper_scissors'))
    dp.message.register(process_yes_answer,
                        F.text == LEXICON_RU['yes_button'], RockPaperFSM.processing_rock_paper)
    dp.message.register(process_no_answer,
                        F.text == LEXICON_RU['no_button'], RockPaperFSM.processing_rock_paper)
    # dp.register_message_handler(process_game_button,
    #                             Text(equals=[LEXICON_RU['rock'],
    #                                          LEXICON_RU['paper'],
    #                                          LEXICON_RU['scissors']]), state=RockPaperFSM.processing_rock_paper)
