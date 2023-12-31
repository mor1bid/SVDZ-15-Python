# Семинар 3 Задача 6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного 
# слова был один пробел между ним и номером строки.

import logging
from sys import argv

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a", encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")

def textprocess(message):
    "Метод отсортировки введённого текста согласно Unicode, с новой строки. Текст не должен содержать ничего кроме букв."
    logging.info(f'Текст получен: {message}')
    try:
        if not message:
            raise ValueError()
        co = 1
        if type(message) is not list:
            message = message.split()
        for line in message:
            spy = sum(1 for ch in line if not ch.isalpha())
            print(co, ". ", line)
            if spy != 0:
                logging.warning('Посторонние символы при вводе текста!')
            co += 1
    except ValueError:
        logging.error('Текст не найден!')
    logging.info(f'{textprocess.__name__}: Работа успешно выполнена!')

script, *message = argv

if __name__ == '__main__':
    textprocess(message)