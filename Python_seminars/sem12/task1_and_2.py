# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов

# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.
import json


class Factorial:
    def __init__(self, limit: int):
        self.limit = limit
        self.result = []

    def __call__(self, count: int):
        fact = 1
        list_fact = []
        for i in range(1, count + 1):
            fact *= i
            list_fact.append(fact)
        self.result.append(list_fact[-self.limit:])
        return fact

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('result.json', 'w', encoding='UTF-8') as file:
            json.dump(self.result, file)


a = Factorial(3)

with a as fact:
    fact(5)
