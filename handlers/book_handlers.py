from copy import deepcopy

from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from databases.database import user_dict_template, users_db
from keyboards.bookmarks_kb import (create_bookmarks_keyboard,
                                    create_edit_keyboard)
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from app.bookdbworker import get_page

lenbook = 13


# Этот хэндлер будет срабатывать на команду "/beginning"
# и отправлять пользователю первую страницу книги с кнопками пагинации
async def process_beginning_command(message: Message):
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    users_db[message.from_user.id]['page'] = 1
    text = get_page(users_db[message.from_user.id]['page'])
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{users_db[message.from_user.id]["page"]}/{lenbook}',
            'forward'))


# Этот хэндлер будет срабатывать на команду "continue"
# и отправлять пользователю страницу книги, на которой пользователь
# остановился в процессе взаимодействия с ботом
async def process_continue_command(message: Message):
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    text = get_page(users_db[message.from_user.id]['page'])
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{users_db[message.from_user.id]["page"]}/{lenbook}',
            'forward'))


# Этот хэндлер будет срабатывать на команду "/bookmarks"
# и отправлять пользователю список сохраненных закладок,
# если они есть или сообщение о том, что закладок нет
async def process_bookmarks_command(message: Message):
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    if users_db[message.from_user.id]["bookmarks"]:
        await message.answer(
            text=LEXICON_RU[message.text],
            reply_markup=create_bookmarks_keyboard(
                *users_db[message.from_user.id]["bookmarks"]))
    else:
        await message.answer(text=LEXICON_RU['no_bookmarks'])


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время взаимодействия пользователя с сообщением-книгой
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] < lenbook:
        users_db[callback.from_user.id]['page'] += 1
        text = get_page(users_db[callback.from_user.id]['page'])
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                f'{users_db[callback.from_user.id]["page"]}/{lenbook}',
                'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время взаимодействия пользователя с сообщением-книгой
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        text = get_page(users_db[callback.from_user.id]['page'])
        await callback.message.edit_text(
            text=text,
            reply_markup=create_pagination_keyboard(
                'backward',
                f'{users_db[callback.from_user.id]["page"]}/{lenbook}',
                'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с номером текущей страницы и добавлять текущую страницу в закладки
async def process_page_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].add(
        users_db[callback.from_user.id]['page'])
    await callback.answer('Страница добавлена в закладки!')


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок
async def process_bookmark_press(callback: CallbackQuery):
    text = get_page(int(callback.data))
    users_db[callback.from_user.id]['page'] = int(callback.data)
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{users_db[callback.from_user.id]["page"]}/{lenbook}',
            'forward'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "редактировать" под списком закладок
async def process_edit_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU[callback.data],
        reply_markup=create_edit_keyboard(
            *users_db[callback.from_user.id]["bookmarks"]))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "отменить" во время работы со списком закладок (просмотр и редактирование)
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['cancel_text'])
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# с закладкой из списка закладок к удалению
async def process_del_bookmark_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['bookmarks'].remove(
        int(callback.data[:-3]))
    if users_db[callback.from_user.id]['bookmarks']:
        await callback.message.edit_text(
            text=LEXICON_RU['/bookmarks'],
            reply_markup=create_edit_keyboard(
                *users_db[callback.from_user.id]["bookmarks"]))
    else:
        await callback.message.edit_text(text=LEXICON_RU['no_bookmarks'])
    await callback.answer()


# Функция для регистрации хэндлеров пользователя в диспетчере
def register_book_handlers(dp: Dispatcher):
    dp.message.register(process_beginning_command, Command('beginning'))
    dp.message.register(process_continue_command, Command('continue'))
    dp.message.register(process_bookmarks_command, Command('bookmarks'))

    dp.callback_query.register(process_forward_press, F.text == "forward")
    dp.callback_query.register(process_backward_press, F.text == "backward")
    dp.callback_query.register(process_page_press,
                               lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
    dp.callback_query.register(process_bookmark_press, lambda x: x.data.isdigit())
    dp.callback_query.register(process_edit_press, F.text == "edit_bookmarks")
    dp.callback_query.register(process_cancel_press, F.text == "cancel")
    dp.callback_query.register(process_del_bookmark_press,
                               lambda x: 'del' in x.data and x.data[:-3].isdigit())
