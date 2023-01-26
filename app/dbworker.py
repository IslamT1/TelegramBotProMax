import sqlite3

conn = sqlite3.connect("slovarbr.db")
cursor = conn.cursor()


def get_cursor():
    return cursor


def get_links(search_query: str = None):
    """
        Получает список слов и их переводы из базы данных.
        Функция ищет слова в двух таблицах slovarrkb и slovarkbr
        и возвращает до 50 результатов, соответствующих поисковому запросу.
        Если поисковый запрос не указан, функция возвращает первые 50 результатов
        из обеих таблиц, отсортированные по слову.

        Параметры:
        search_query (str, необязательный): слово для поиска. По умолчанию нет.

        Возвращает:
        список: список кортежей, содержащих идентификатор слова, слово и перевод.
    """
    if search_query:
        statement = f"""SELECT _id, slovo, perevod FROM slovarrkb WHERE slovo LIKE '{search_query}%'
                        UNION ALL
                        SELECT _id + 100000, slovo, perevod FROM slovarkbr WHERE slovo LIKE '{search_query}%'
                        ORDER BY slovo
                        LIMIT 50"""
    else:
        statement = f"""SELECT _id, slovo, perevod FROM slovarrkb
                        UNION ALL
                        SELECT _id + 100000, slovo, perevod FROM slovarkbr
                        ORDER BY slovo
                        LIMIT 50"""
    result = cursor.execute(statement)
    return result.fetchall()
