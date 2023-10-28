from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

available_food_names = ["суши", "спагетти", "хачапури"]
available_food_sizes = ["маленькую", "среднюю", "большую"]


class OrderFood(StatesGroup):
    waiting_for_food_name = State()
    waiting_for_food_size = State()


# Обратите внимание: есть второй аргумент
async def food_start(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardBuilder()
    for name in available_food_names:
        keyboard.add(types.KeyboardButton(text=name))
    await message.answer("Выберите блюдо:", reply_markup=keyboard.as_markup(resize_keyboard=True))
    await state.set_state(OrderFood.waiting_for_food_name)


async def food_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_food_names:
        await message.answer("Пожалуйста, выберите блюдо, используя клавиатуру ниже.")
        return
    await state.update_data(chosen_food=message.text.lower())

    keyboard = ReplyKeyboardBuilder()
    for size in available_food_sizes:
        keyboard.add(types.KeyboardButton(text=size))
    await state.set_state(OrderFood.waiting_for_food_size)
    await message.answer("Теперь выберите размер порции:", reply_markup=keyboard.as_markup(resize_keyboard=True))


async def food_size_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_food_sizes:
        await message.answer("Пожалуйста, выберите размер порции, используя клавиатуру ниже.")
        return
    user_data = await state.get_data()
    await message.answer(f"Вы заказали {message.text.lower()} порцию {user_data['chosen_food']}.",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


def register_handlers_food(dp: Dispatcher):
    dp.message.register(food_start, Command("food"))  # , state="*")
    dp.message.register(food_chosen, OrderFood.waiting_for_food_name)
    dp.message.register(food_size_chosen, OrderFood.waiting_for_food_size)
