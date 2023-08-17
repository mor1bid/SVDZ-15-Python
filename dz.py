# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import logging
from sys import argv

# Семинар 3 Задача 6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного 
# слова был один пробел между ним и номером строки.

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w", encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")

def sortext(message):
    "Метод отсортировки введённого текста с новой строки. Текст не должен содержать ничего кроме букв."
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

script, *message = argv
# message = input("\n6. Введите желаемый текст через пробел (текст не может содержать ничего кроме букв!)\n: ")
sortext(message)
logging.info('Работа успешно выполнена!')

# Семинар 10 Задача 2
# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании
# экземпляра. У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectan:
    "Класс обработки двух переменных и вычисления площади и периметра четырёхсторонней фигуры"
    def __new__(cls, lng, wdt, figur = ''):
        "Получение переменных от пользователя, создание новой фигуры"
        respawn = super().__new__(cls)
        respawn.lng = int(lng)
        respawn.wdt = int(wdt)
        if lng == wdt:
            respawn.figur = figur + 'Квадрат'
        else:
            respawn.figur = figur + 'Прямоугольник'
        logging.info(f'Значение длины: {lng}\nЗначение ширины: {wdt}\nФигура: {figur}')
        return respawn
    def area(respawn):
        "Вычисление площади фигуры"
        area = respawn.lng * respawn.wdt
        return area
    def perimet(respawn):
        "Вычисление периметра фигуры"
        perimet = 2 * (respawn.lng + respawn.wdt)
        return perimet
    def __str__(self, respawn):
        "Вывод результата"
        logging.info(f'Фигура: {respawn.figur}\nЗначение площади: {self.area()}\nЗначение периметра: {self.perimet()}')
        return f'Площадь = {self.area()}\nПериметр = {self.perimet()}'

paramets = input("\n5. Введите желаемую длину и ширину прямоугольника через пробел (значения должны быть больше 0)\n: ")
paramets = paramets.split()
try:
    spy = sum(1 for dig in paramets if int(dig) < 0 or not dig.isdigit())
    if spy != 0:
        raise ValueError()
except ValueError:
    logging.error('Невозможно создать фигуру. Некорректное значение введённого параметра!')
ex = Rectan(paramets[0], paramets[-1])
ex2 = Rectan(25, 25)
print(f'\nПример 1 (длина: {ex.lng}, ширина: {ex.wdt}, {ex.figur}):\n{ex}\n\nПример 2 (длина: {ex2.lng}, ширина: {ex2.wdt}, {ex2.figur}):\n{ex2}\n\nСумма периметров двух фигур: {ex.perimet()} + {ex2.perimet()} =  {ex.perimet() + ex2.perimet()}\nРазность периметров двух фигур: {ex.perimet()} - {ex2.perimet()} = {ex.perimet() - ex2.perimet()}')
if ex.area() < ex2.area():
    print(f'\n6. Площадь первой фигуры меньше второй.')
elif ex.area() > ex2.area():
    print(f'\n6. Площадь первой фигуры больше второй.')
elif ex.area() == ex2.area():
    print(f'\n6. Площади фигур равны.')
if ex.area() != ex2.area():
    print(f'Площади фигур не равны.')
print(f'\nДокументация класса: {Rectan.__doc__ = }')
print(f'Документация экземпляра: {ex.__doc__ = }')
print(f'Документация метода: {Rectan.perimet.__doc__ = }')
logging.info('Работа успешно выполнена!')