# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.
import logging


logging.basicConfig(filename='error.log', level=logging.ERROR)

try:
    10 / 0
except ZeroDivisionError:
    logging.error('Делим на 0')
