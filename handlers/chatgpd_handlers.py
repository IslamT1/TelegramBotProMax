from aiogram import Dispatcher, types
import os
import openai

async def chatgpd(message: types.Message, ):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=message.text,
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=["\n"]
    )
    await message.reply(text=response)



def register_chatgpd_handlers(dp: Dispatcher):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # dp.register_inline_handler(inline_handler, state="*")
    # dp.register_chosen_inline_handler(chosen_handler, state="*")
    dp.register_message_handler(chatgpd)