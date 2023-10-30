import asyncio
import logging
import openai

from app.dbworker import get_cursor

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode

from keyboards.set_menu import set_main_menu
from handlers import book_handlers, other_handlers
from handlers.food import register_handlers_food
from handlers.common import register_handlers_common
from handlers.calculator import register_handlers_calc
from handlers.inline_mode import register_inline_handlers
from handlers.chatgpd_handlers import register_chatgpd_handlers
from handlers.rock_paper_scissors_handlers import register_user_handlers

from config_data.config import Config, load_config

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_handlers_common(dp)
    register_handlers_calc(dp)
    register_handlers_food(dp)
    register_inline_handlers(dp)
    register_user_handlers(dp)
    register_chatgpd_handlers(dp)


# Функция для регистрации всех роутеров
def register_all_routers(dp):
    dp.include_router(book_handlers.router)
    dp.include_router(other_handlers.router)


# Функция конфигурирования и запуска бота
async def main():
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s - %(lineno)d - (%(filename)s).%(funcName)s(%("
               "lineno)d)",
    )
    # Выводим информацию о начале запуска бота
    logger.info("Starting bot")

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=config.tg_bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    openai.api_key = config.tg_bot.openai_token

    # Регистрируем все хэндлеры
    register_all_handlers(dp)

    # Регистрируем все роутеры
    register_all_routers(dp)

    # Установка команд бота
    await set_main_menu(bot)

    # Запуск поллинга
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()
        get_cursor().close()


if __name__ == '__main__':
    try:
        # Запускаем функцию main
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')
