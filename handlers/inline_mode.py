import logging
from aiogram import Dispatcher, types
from aiogram.utils.markdown import quote_html
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

async def inline_handler(query: types.InlineQuery):
    slova = get_links(query.query or None)
    if len(slova) == 0:
        switch_text = "Не найдено слов по данному запросу."
        return await query.answer([],
                                cache_time=60,
                                is_personal=True,
                                switch_pm_parameter="qwer",
                                switch_pm_text=switch_text)
    articles = [types.InlineQueryResultArticle(
                id=item[0],
                title=item[1],
                description=re.sub(CLEANR, '', item[2]),
                # url=f"https://youtu.be/{item[0]}",
                hide_url=True,
                # thumb_url=f"https://img.youtube.com/vi/{item[0]}/1.jpg",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"<b>{item[1]}</b> - {fix_html(item[2])}",
                    parse_mode="HTML"
                )) for item in slova]
    await query.answer(articles,
                       cache_time=60,
                       is_personal=True)


# async def inline_handler(query: types.InlineQuery):
#     user_links = dbworker.get_links(query.from_user.id, query.query or None)
#     if len(user_links) == 0:
#         switch_text = "У вас нет сохранённых ссылок. Добавить »»" \
#             if len(query.query) == 0 \
#             else "Не найдено ссылок по данному запросу. Добавить »»"
#         return await query.answer(
#             [], cache_time=60, is_personal=True,
#             switch_pm_parameter="add", switch_pm_text=switch_text)
#     articles = [types.InlineQueryResultArticle(
#         id=item[0],
#         title=item[1],
#         description=f"https://youtu.be/{item[0]}",
#         url=f"https://youtu.be/{item[0]}",
#         hide_url=False,
#         thumb_url=f"https://img.youtube.com/vi/{item[0]}/1.jpg",
#         input_message_content=types.InputTextMessageContent(
#             message_text=f"<b>{quote_html(item[1])}</b>\nhttps://youtu.be/{item[0]}",
#             parse_mode="HTML"
#         )
#     ) for item in user_links]
#     await query.answer(articles, cache_time=60, is_personal=True,
#                        switch_pm_text="Добавить ссылку »»", switch_pm_parameter="add")


# Хэндлер для сбора статистики (не забудьте включить сбор у @BotFather)
async def chosen_handler(chosen_result: types.ChosenInlineResult):
    logging.info(f"Chosen query: {chosen_result.query},"
                 f" from user: {chosen_result.from_user.id}")


def register_inline_handlers(dp: Dispatcher):
    dp.register_inline_handler(inline_handler, state="*")
    dp.register_chosen_inline_handler(chosen_handler, state="*")