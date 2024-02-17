# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class MyError(Exception):
    def __init__(self, msg, message):
        self.message = message
        self.msg = msg

    def __str__(self):
        return f'{self.msg}: {self.message}'


class LevelError(MyError):
    def __init__(self, message):
        super().__init__('Level Error', message)


class AccessError(MyError):
    def __init__(self, message):
        super().__init__('Access Error', message)