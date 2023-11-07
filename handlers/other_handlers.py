from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

from lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message(Command(commands='lost_points_calc'))
async def lost_points(message: Message):
    bt = InlineKeyboardButton(text=LEXICON_RU['open'],
                              web_app=WebAppInfo(url="https://islamtambiev.github.io/Lost-Points-Calculator/"))
    kb = InlineKeyboardMarkup(inline_keyboard=[[bt]])
    await message.answer(text=LEXICON_RU['lost_points_calc'], reply_markup=kb)


# Хэндлер для текстовых сообщений, которые не попали в другие хэндлеры
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])


router.message.register(send_answer)  # , state="*")
