# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import randint
from random import choice


MIN_LEN = 4
MAX_LEN = 7


def names():
    vowels = ['у', 'а', 'э', 'о', 'ю', 'е', 'я', 'ы', 'и', 'ё']
    cons = [
        'ш', 'з', 'ч', 'щ', 'ъ', 'х', 'р', 'ц', 'ь', 'п', 'ж',
        'л', 'ф', 'м', 'с', 'в', 'б', 'н', 'й', 'т', 'к', 'д', 'г'
    ]
    name_len = randint(MIN_LEN, MAX_LEN)
    start_letter = randint(0, 1)
    result_name = ''
    if start_letter:
        result_name += choice(list(vowels))
    else:
        result_name += choice(list(cons))
    for i in range(1, name_len):
        if result_name[i - 1] in vowels:
            result_name += choice(list(cons))
        else:
            result_name += choice(list(vowels))
    return result_name.capitalize()


def file_input(lines_count: int, file_name: str):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for _ in range(lines_count):
            file.write(f'{names()}\n')


file_input(10, 'names.txt')
