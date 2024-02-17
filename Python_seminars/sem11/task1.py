# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time


class MyString(str):
    def __new__(cls, value, author=None):
        return super().__new__(cls, value)

    def __init__(self, value, author=None):
        self.author = author
        self.time = time.ctime(time.time())


my_string = MyString('text', 'Me')
print(my_string)
print(my_string.author)
print(my_string.time)
