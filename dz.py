# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import logging
# from z1 import sortext
# from z2 import mathprocess

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w+", encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")

message = input("\n1. Введите желаемый текст через пробел (текст не может содержать ничего кроме букв!)\n: ")
from z1 import sortext
sortext(message)
paramets = input("\n2. Введите желаемую длину и ширину прямоугольника через пробел (значения должны быть больше 0)\n: ")
from z2 import mathprocess
mathprocess(paramets)
