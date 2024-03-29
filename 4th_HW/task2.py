# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
#
# Пример использования.
# На входе:
#
#
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе:
#
#
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

import typing


def key_params(**kwargs):
    """
    Мой вариант решения
    :param kwargs:
    :return:
    """
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, typing.Hashable):
            result[value] = key
        else:
            result[str(value)] = key
    return result


params = key_params(a=None, b='', c=[], d={})
print(params)

# def key_params(**kwargs):
#     """
#     "Эталонное решение"
#     :param kwargs:
#     :return:
#     """
#     result_2 = {}
#     for key, value in kwargs.items():
#         if isinstance(value, (int, str, float, bool, tuple)):
#             result_2[value] = key
#         else:
#             result_2[str(value)] = key
#     return result_2
