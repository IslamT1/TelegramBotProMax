from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

user_data = {}


# calc - префикс, action - название аргумента, которым будем передавать значение
# callback_numbers = CallbackData("calc", "action")

class CalcCallbackFactory(CallbackData, prefix="calc"):
    action: str


def get_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text=" 7", callback_data=CalcCallbackFactory(action="7").pack()),
         types.InlineKeyboardButton(text=" 8 ", callback_data=CalcCallbackFactory(action="8").pack()),
         types.InlineKeyboardButton(text=" 9 ", callback_data=CalcCallbackFactory(action="9").pack()),
         types.InlineKeyboardButton(text=" <= ", callback_data=CalcCallbackFactory(action="<").pack())],
        [types.InlineKeyboardButton(text=" 4 ", callback_data=CalcCallbackFactory(action="4").pack()),
         types.InlineKeyboardButton(text=" 5 ", callback_data=CalcCallbackFactory(action="5").pack()),
         types.InlineKeyboardButton(text=" 6 ", callback_data=CalcCallbackFactory(action="6").pack()),
         types.InlineKeyboardButton(text=" - ", callback_data=CalcCallbackFactory(action="-").pack())],
        [types.InlineKeyboardButton(text=" 1 ", callback_data=CalcCallbackFactory(action="1").pack()),
         types.InlineKeyboardButton(text=" 2 ", callback_data=CalcCallbackFactory(action="2").pack()),
         types.InlineKeyboardButton(text=" 3 ", callback_data=CalcCallbackFactory(action="3").pack()),
         types.InlineKeyboardButton(text=" + ", callback_data=CalcCallbackFactory(action="+").pack())],
        [types.InlineKeyboardButton(text=" / ", callback_data=CalcCallbackFactory(action="/").pack()),
         types.InlineKeyboardButton(text=" 0 ", callback_data=CalcCallbackFactory(action="0").pack()),
         types.InlineKeyboardButton(text=" * ", callback_data=CalcCallbackFactory(action="*").pack()),
         types.InlineKeyboardButton(text=" = ", callback_data=CalcCallbackFactory(action="=").pack()), ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def update_num_text(message: types.Message, new_value: str):
    with suppress(TelegramBadRequest):
        await message.edit_text(f"{new_value}", reply_markup=get_keyboard())
    # pass


async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = ["", "", ""]
    await message.answer("0", reply_markup=get_keyboard())


async def callbacks_num_change(call: types.CallbackQuery, callback_data: CalcCallbackFactory):
    user_value = user_data.get(call.from_user.id, ["", "", ""])
    action = callback_data.action
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
    dp.callback_query.register(callbacks_num_change, CalcCallbackFactory.filter())
