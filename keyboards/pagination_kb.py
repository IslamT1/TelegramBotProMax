from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU


# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    pagination_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    # Наполняем клавиатуру кнопками
    pagination_kb.row(*[InlineKeyboardButton(LEXICON_RU[button] if button in LEXICON_RU else button,
                                             callback_data=button) for button in buttons])
    return pagination_kb
