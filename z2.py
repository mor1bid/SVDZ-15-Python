# Семинар 10 Задача 2
# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании
# экземпляра. У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

import logging
from sys import argv

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
    
def mathprocess(paramets):
    if type(paramets) is not list:
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
    logging.info(f'{mathprocess().__name__}: Работа успешно выполнена!')

script, *paramets = argv
mathprocess(paramets)