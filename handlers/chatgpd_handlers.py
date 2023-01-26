import openai

from aiogram import Dispatcher, types
from aiogram.utils.exceptions import CantParseEntities
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class ChatGPDFSM(StatesGroup):
    # Состояния
    processing_message = State()


async def process_start_command(message: types.Message):
    await message.reply("Чем могу помочь?\nДля выхода из чата с ChatGPD введи /stop.")
    await ChatGPDFSM.processing_message.set()


async def process_message(message: types.Message):
    response = await generate_response(message.text)
    try:
        await message.reply(text=response)
    except CantParseEntities as e:
        print(message.text)
        print(response)
        print(e)


async def process_stop_command(message: types.Message, state: FSMContext):
    await message.reply("Дай знать если тебе понадобится помощь в будущем.")
    await state.finish()


async def generate_response(prompt: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6,
    )
    # print("#################################################\nВопрос: ", prompt, "\nОтвет: ",
    #       str(response['choices'][0]['text']))
    return response['choices'][0]['text']


def register_chatgpd_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['chatgpd'])
    dp.register_message_handler(process_stop_command, commands=['stop'], state=ChatGPDFSM.processing_message)
    dp.register_message_handler(process_message, state=ChatGPDFSM.processing_message)
