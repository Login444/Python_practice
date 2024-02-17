# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def get_dict(new_dict: dict, key, default_value):
    try:
        return new_dict[key]
    except KeyError as exc:
        return default_value


dict1 = {1: 'one', 2: 'two', 3: 'three'}


print(get_dict(dict1, 1, 'zero'))
print(get_dict(dict1, 4, 'zero'))
