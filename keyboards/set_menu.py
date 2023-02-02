from aiogram import Dispatcher
from aiogram.types import BotCommand


# Регистрация команд, отображаемых в интерфейсе Telegram
async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        BotCommand(command="/start", description="Перезапустить"),
        BotCommand(command="/help", description="Справка по работе бота"),
        BotCommand(command="/calc", description="Калькулятор"),
        BotCommand(command="/dict", description="Словарь"),
        BotCommand(command="/chatgpd", description="ChatGPD"),
        BotCommand(command="/rock_paper_scissors", description="Камень, ножницы, бумага"),
        BotCommand(command="/food", description="Заказать блюда"),
        BotCommand(command="/stop", description="Сбросить текущее состояние"),
        BotCommand(command='/beginning', description='В начало книги'),
        BotCommand(command='/continue', description='Продолжить чтение'),
        BotCommand(command='/bookmarks', description='Мои закладки'),
    ]
    await dp.bot.set_my_commands(main_menu_commands)
