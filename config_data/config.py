from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    db_name: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_pass: str  # Пароль к базе данных


@dataclass
class TgBotConfig:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота
    openai_token: str  # Токен для доступа к chatgpd


@dataclass
class Config:
    tg_bot: TgBotConfig
    db: DatabaseConfig


def load_config() -> Config:
    """
    Load the configuration settings from the environment variables and create a Config object.

    Returns:
        Config: The configuration object containing the loaded settings.
    """
    # Создаем экземпляр класса Env
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env()

    # Создаем экземпляр класса Config и наполняем его данными из переменных окружения
    return Config(tg_bot=TgBotConfig(token=env('BOT_TOKEN'),
                                     admin_ids=list(map(int, env.list('ADMIN_IDS'))),
                                     openai_token=env('OPEN_AI_TOKEN')),
                  db=DatabaseConfig(db_name=env('DB_NAME'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_pass=env('DB_PASS')))
