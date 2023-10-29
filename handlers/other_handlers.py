from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Хэндлер для текстовых сообщений, которые не попали в другие хэндлеры
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])


router.message.register(send_answer)  # , state="*")
