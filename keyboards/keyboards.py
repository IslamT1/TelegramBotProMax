from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[
        button_yes,
        button_no,
    ]],
    one_time_keyboard=True,
    resize_keyboard=True)

# # Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
# yes_no_kb.add(button_yes, button_no)

# Создаем игровую клавиатуру с кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜"
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[
        button_1,
        button_2,
        button_3,
    ]],
    resize_keyboard=True)

# # Располагаем кнопки в клавиатуре одну под другой в 3 ряда
# game_kb.add(button_1).add(button_2).add(button_3)
