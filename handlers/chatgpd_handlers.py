from aiogram import Dispatcher, types
from config_data.config import load_config
import openai


async def chatgpd(message: types.Message, ):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6,
    )
    await message.reply(text=response['choices'][0]['text'])


def register_chatgpd_handlers(dp: Dispatcher):
    openai.api_key = load_config().tg_bot.openai_token

    # dp.register_inline_handler(inline_handler, state="*")
    # dp.register_chosen_inline_handler(chosen_handler, state="*")
    dp.register_message_handler(chatgpd)
