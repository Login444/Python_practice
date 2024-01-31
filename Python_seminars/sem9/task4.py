# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def deco_with_params(count: int):
    result = []
    def outer(func):
        def inner(*args, **kwargs):
            for _ in range(count):
                result.append(func(*args, *kwargs))
            return result

        return inner