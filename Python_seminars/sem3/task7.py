# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

my_str = input('Введите текст: ')
my_set = set(my_str)
my_dict = dict()


# for i in my_set:
#     count = 0
#     for j in range(len(my_str)):
#         if my_str[j] == i:
#             count += 1
#     my_dict[i] = count
#
# print(my_dict)

# for i in my_set:
#     my_dict.setdefault(i, my_str.count(i))
#
# print(my_dict)

for i in my_str:
    my_dict[i] = my_dict.get(i, 0) + 1
print(my_dict)