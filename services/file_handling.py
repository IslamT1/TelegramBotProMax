BOOK_PATH = 'book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    c = [',', '.', '!', ':', ';', '?']
    txt = ''
    end = start + size - 1 if len(text) > start + size - 1 else len(text) - 1
    for i in range(end, start + 1, -1):
        if text[i] in c:
            if text[i - 1] in c:
                continue
            elif end >= i + 1 and text[i + 1] in c:
                continue
            txt = text[start:i + 1]
            break
    return txt, len(txt)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read().lstrip()
        i = 1
        n = 0
        x = 1000
        while x > 500:
            t, x = _get_part_text(text, n, PAGE_SIZE)
            book[i] = t.lstrip()
            if not x:
                break
            n += x
            i += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
