from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
# from aiogram.filters.exception import MessageNotModified
from contextlib import suppress

user_data = {}

# calc - префикс, action - название аргумента, которым будем передавать значение
callback_numbers = CallbackData("calc", "action")


def get_keyboard():
    buttons = [
        types.InlineKeyboardButton(text=" 7", callback_data=callback_numbers.new(action="7")),
        types.InlineKeyboardButton(text=" 8 ", callback_data=callback_numbers.new(action="8")),
        types.InlineKeyboardButton(text=" 9 ", callback_data=callback_numbers.new(action="9")),
        types.InlineKeyboardButton(text=" <= ", callback_data=callback_numbers.new(action="<")),
        types.InlineKeyboardButton(text=" 4 ", callback_data=callback_numbers.new(action="4")),
        types.InlineKeyboardButton(text=" 5 ", callback_data=callback_numbers.new(action="5")),
        types.InlineKeyboardButton(text=" 6 ", callback_data=callback_numbers.new(action="6")),
        types.InlineKeyboardButton(text=" - ", callback_data=callback_numbers.new(action="-")),
        types.InlineKeyboardButton(text=" 1 ", callback_data=callback_numbers.new(action="1")),
        types.InlineKeyboardButton(text=" 2 ", callback_data=callback_numbers.new(action="2")),
        types.InlineKeyboardButton(text=" 3 ", callback_data=callback_numbers.new(action="3")),
        types.InlineKeyboardButton(text=" + ", callback_data=callback_numbers.new(action="+")),
        types.InlineKeyboardButton(text=" / ", callback_data=callback_numbers.new(action="/")),
        types.InlineKeyboardButton(text=" 0 ", callback_data=callback_numbers.new(action="0")),
        types.InlineKeyboardButton(text=" * ", callback_data=callback_numbers.new(action="*")),
        types.InlineKeyboardButton(text=" = ", callback_data=callback_numbers.new(action="=")),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    keyboard.add(*buttons)
    return keyboard


async def update_num_text(message: types.Message, new_value: str):
    # with suppress(MessageNotModified):
    #     await message.edit_text(f"{new_value}", reply_markup=get_keyboard())
    pass


async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = ["", "", ""]
    await message.answer("0", reply_markup=get_keyboard())


async def callbacks_num_change(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, ["", "", ""])
    action = callback_data["action"]
    if user_value[1] == "":
        v = 0
    else:
        v = 2

    match action:
        case "1":
            user_value[v] = user_value[v] + "1"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "2":
            user_value[v] = user_value[v] + "2"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "3":
            user_value[v] = user_value[v] + "3"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "4":
            user_value[v] = user_value[v] + "4"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "5":
            user_value[v] = user_value[v] + "5"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "6":
            user_value[v] = user_value[v] + "6"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "7":
            user_value[v] = user_value[v] + "7"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "8":
            user_value[v] = user_value[v] + "8"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "9":
            user_value[v] = user_value[v] + "9"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "0":
            user_value[v] = user_value[v] + "0"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "+":
            user_value[1] = "+"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "-":
            user_value[1] = "-"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "*":
            user_value[1] = "*"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "/":
            user_value[1] = "/"
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "<":
            if user_value[2] == "" and user_value[1] != "":
                user_value[1] = ""
            else:
                user_value[v] = user_value[v][:-1]
            user_data[call.from_user.id] = user_value
            x = user_value[0] + " " + user_value[1] + " " + user_value[2]
            await update_num_text(call.message, x)

        case "=":
            if user_value[2] == "0" and user_value[1] == "/":
                await update_num_text(call.message, "На ноль делить не советую")
            else:
                x = user_value[0] + " " + user_value[1] + " " + user_value[2]
                x = x + " = " + str(eval(x))
                await update_num_text(call.message, x)

    await call.answer('Вау', show_alert=False)


def register_handlers_calc(dp: Dispatcher):
    dp.message.register(cmd_numbers, Command(commands="calc"))
    dp.register_callback_query_handler(callbacks_num_change, callback_numbers.filter(
        action=["7", "8", "9", "<", "4", "5", "6", "-", "1", "2", "3", "+", "/", "0", "*", "="]))
