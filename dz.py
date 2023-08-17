# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import logging
import sys

# Семинар 3 Задача 6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного 
# слова был один пробел между ним и номером строки.

def sortext(message):
    logging.info('Программа для отсортировки введённого текста с новой строки.\nТекст не может содержать ничего кроме букв.')
    try:
        if not message:
            raise ValueError('suka')
        co = 1
        for line in message.split():
            spy = sum(1 for ch in line if not ch.isalpha())
            print(co, ". ", line)
            if spy != 0:
                logging.warning('Посторонние символы при вводе текста!')
            co += 1
    except ValueError:
        logging.error('Текст не найден!')

if __name__ == "__main__":
    cmd = sys.argv[0]
    sortext(cmd)

message = input("\n6. Введите желаемый текст через пробел (текст не может содержать ничего кроме букв!)\n: ")
sortext(message)

# Семинар 10 Задача 2
# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании
# экземпляра. У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectan:
    logging.info('Rectan - класс обработки двух переменных и вычисления площади и периметра четырёхсторонней фигуры')
    "Класс обработки двух переменных и вычисления площади и периметра четырёхсторонней фигуры"
    def __new__(cls, lng, wdt, figur = ''):
        "Получение переменных от пользователя, создание новой фигуры"
        worker = super().__new__(cls)
        worker.lng = int(lng)
        worker.wdt = int(wdt)
        if lng == wdt:
            worker.figur = figur + 'Квадрат'
        else:
            worker.figur = figur + 'Прямоугольник'
        return worker
    def area(worker):
        "Вычисление площади фигуры"
        area = worker.lng * worker.wdt
        return area
    def perimet(worker):
        "Вычисление периметра фигуры"
        perimet = 2 * (worker.lng + worker.wdt)
        return perimet
    def __str__(self):
        "Вывод результата"
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