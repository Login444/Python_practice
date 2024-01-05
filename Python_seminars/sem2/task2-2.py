# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный

# Добавьте в список повторяющиеся элементы и сравните на результаты

data = [1, 'hello', 555555555555555, 'world', True, 1.2, 1]

for i in data:
    print(data.index(i) + 1, i, id(i), i.__sizeof__(), hash(i))
    if isinstance(i, int):
        print('Число целое')
    elif isinstance(i, str):
        print('Это строка')
