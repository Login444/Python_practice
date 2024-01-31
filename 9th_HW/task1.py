# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке,
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
#
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
#
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:
#
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
#
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
#
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json.
# Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация
# о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

import csv
import json
import random


def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='', encoding='utf-8', ) as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


def save_to_json(func):
    def wrapper(file_name):
        res = []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                result = {"parameters": [a, b, c], "result": roots}
                res.append(result)
        with open('results.json', 'w', encoding='utf-8') as file:
            json.dump(res, file, indent=4)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr < 0:
        return None
    elif discr == 0:
        return -b / (2 * a)
    else:
        root_1 = (-b + discr ** 0.5) / 2 * a
        root_2 = (-b - discr ** 0.5) / 2 * a
        return root_1, root_2
