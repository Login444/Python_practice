# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


num = 255


def convert_to_base_hex(number: int):
    result = ''
    base_dictionary = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while number > 0:
        remainder = number % 16
        if remainder > 9:
            result = str(base_dictionary.get(remainder)) + result
            number = number // 16
        else:
            result = str(remainder) + result
            number = number // 16
    return result


print(f'Шестнадцатеричное представление числа: {convert_to_base_hex(num)}')
print(f'Проверка результата: {hex(num)}')
