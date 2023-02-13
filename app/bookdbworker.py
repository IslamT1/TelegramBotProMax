import sqlite3

conn = sqlite3.connect("book.db")
cursor = conn.cursor()


def get_cursor():
    return cursor


def get_page(page: int):
    if page:
        statement = f"""SELECT value FROM data WHERE key == {page}"""
        result = cursor.execute(statement).fetchall()
    else:
        result = ''

    return result
