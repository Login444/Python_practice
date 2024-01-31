# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.
from random import randint, choice

_res_dict = {}


def puzzle(text: str, variants: list[str], count: int):
    print(text)
    variant_v = list(map(lambda x: x.lower(), variants))
    while count:
        user_input = input("Вариант ответа: ").lower()
        if user_input in variant_v:
            count -= 1
            return count
        else:
            print('No.')
        count -= 1
    return 0


# � Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.


# def puzzle_dict():
#     in_dict = {
#         "Зимой и летом одним цветом": ["ель", "пихта", "доллар"],
#         "Висит груша нельзя скушать": ["лампа", "лампочка"],
#         "Не лает не кусает в дом не пускает": ["замок"]
#     }
#
#     for key, value in in_dict.items():
#         puzzle(key, value, randint(3, 6))


def puzzle_solut(count: 3):
    dict_puzzle = {
        "Зимой и летом одним цветом": ["ель", "пихта", "доллар"],
        "Висит груша нельзя скушать": ["лампа", "лампочка"],
        "Не лает не кусает в дом не пускает": ["замок", "гусь"]
    }
    count = count if count < len(dict_puzzle) else len(dict_puzzle)
    for _ in range(count):
        cur_puzzle = choice(list(dict_puzzle))
        cur_value = dict_puzzle.pop(cur_puzzle)
        result = puzzle(cur_puzzle, cur_value, randint(1, 3))
        result_info(cur_puzzle, result)
    puzzle_count_print()


# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное
# выражение.


def result_info(text_puzzle: str, count: int):
    _res_dict[text_puzzle] = count


def puzzle_count_print():
    for guess_text, guess_count in _res_dict.items():
        print(f'Загадку {guess_text} ' + (f'угадали с попытки {guess_count}' if guess_count else 'не угадали'))
