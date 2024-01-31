# Создайте функцию генератор чисел Фибоначчи fibonacci.

def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


f = fibonacci()
for i in range(10):
    print(next(f))
