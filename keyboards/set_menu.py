from aiogram import Dispatcher
from aiogram.types import BotCommand

# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        BotCommand(command="/start", description="Запустить"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/calc", description="Калькулятор"),
        BotCommand(command="/dict", description="Словарь"),
        BotCommand(command="/chatgpd", description="Словарь"),
        BotCommand(command="/rock_paper_scissors", description="Камень, ножницы, бумага"),
        BotCommand(command="/food", description="Заказать блюда"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await dp.bot.set_my_commands(main_menu_commands)