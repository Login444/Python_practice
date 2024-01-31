# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random

MIN_LIM = -1000
MAX_LIM = 1000


def file_input(lines_count: int, file_name: str):
    with open(file_name, 'a', encoding='UTF-8') as file:
        for _ in range(lines_count):
            file.write(f'{random.randint(MIN_LIM, MAX_LIM)} | {random.uniform(MIN_LIM, MAX_LIM)}\n')


file_input(10, 'numbers.txt')
