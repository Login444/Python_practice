# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

test = (1, 'text', '123', [1, 2, 3], 12.5, True, False, -25, -300.5, ['text', 1, 3.5])

dictionary = dict()

for i in test:
    if type(i) in dictionary:
        dictionary[type(i)].append(i)
    else:
        dictionary[type(i)] = [i, ]

print(dictionary)
