import logging
from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.dbworker import get_links
from bs4 import BeautifulSoup
import re

# as recommendation, compile once only
CLEANR = re.compile('<.*?>')


# Для убирания незакрытого тега
def fix_html(text):
    soup = BeautifulSoup(text, "html.parser")
    for item in soup.find_all('strong'):
        if item.findChild():
            item.unwrap()
    return soup


# Инлайн режим
async def inline_handler(query: types.InlineQuery):
    slova = get_links(query.query or None)
    if len(slova) == 0:
        switch_text = "Перейти в бота >>"
        return await query.answer([],
                                  cache_time=60,
                                  is_personal=True,
                                  switch_pm_parameter="qwer",
                                  switch_pm_text=switch_text)
    articles = [types.InlineQueryResultArticle(
        id=item[0],
        title=item[1],
        description=re.sub(CLEANR, '', item[2])[:150],
        hide_url=True,
        # thumb_url=f"https://img.youtube.com/vi/{item[0]}/1.jpg",
        input_message_content=types.InputTextMessageContent(
            message_text=f"<b>{item[1]}</b> - {fix_html(item[2][:5000])}",
            parse_mode="HTML"
        )) for item in slova]
    await query.answer(articles,
                       cache_time=60,
                       is_personal=True)


# Кнопки для открытия инлайн режима
async def switch_to_inline_button(message: types.Message, state: FSMContext):
    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть инлайн режим", switch_inline_query_current_chat='')],
            [InlineKeyboardButton(text="Открыть инлайн в другом чате", switch_inline_query='')],
        ])
    await message.bot.send_message(chat_id=message.chat.id,
                                   text="Нажми на кнопку чтобы открыть инлайн режим.",
                                   reply_markup=inline_kb)
    await state.clear()


# Хэндлер для сбора статистики (не забудьте включить сбор у @BotFather)
async def chosen_handler(chosen_result: types.ChosenInlineResult):
    logging.info(f"Chosen query: {chosen_result.query},"
                 f" from user: {chosen_result.from_user.id}")


def register_inline_handlers(dp: Dispatcher):
    dp.inline_query.register(inline_handler)  # , state="*")
    dp.chosen_inline_result.register(chosen_handler)  # , state="*")
    dp.message.register(switch_to_inline_button, Command("dict"))  # , state="*")
