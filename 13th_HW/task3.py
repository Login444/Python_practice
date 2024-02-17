# В организации есть два типа людей: сотрудники и обычные люди.
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
#
# Фамилия (строка, не пустая)
# Имя (строка, не пустая)
# Отчество (строка, не пустая)
# Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.
#
# Ваша задача:
#
# Создать класс Person,
# который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных и генерировать исключения
# InvalidNameError и InvalidAgeError, если данные неверные.
#
# Создать класс Employee,
# который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#
# Добавить метод get_level в класс Employee,
# который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить,
# что исключения работают корректно при передаче неверных данных.
class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(Exception):
    def __init__(self, u_id):
        self.u_id = u_id

    def __str__(self):
        return f'Invalid id: {self.u_id}. Id should be a 6-digit positive integer between 100000 and 999999.'


class ValidateValue:
    MIN_ID = 100_000
    MAX_ID = 1_000_000

    def __init__(self, value_type: str):
        self.value_type = value_type

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate_value(value)
        setattr(instance, self.param_name, value)

    def validate_value(self, value):
        if self.value_type == 'name':
            if not isinstance(value, str) or value == '':
                raise InvalidNameError(value)
        if self.value_type == 'age':
            if not isinstance(value, int) or value < 0:
                raise InvalidAgeError(value)
        if self.value_type == 'id':
            if not isinstance(value, int) or value not in range(self.MIN_ID, self.MAX_ID):
                raise InvalidIdError(value)


class Person:
    lastname = ValidateValue('name')
    name = ValidateValue('name')
    surname = ValidateValue('name')
    age = ValidateValue('age')

    def __init__(self, lastname: str, name: str, surname: str, age: int):
        self.lastname = lastname.title()
        self.name = name.title()
        self.surname = surname.title()
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.lastname} {self.name} {self.surname}. Возраст: {self.age}.'

    def __repr__(self):
        return f'Person({self.lastname}, {self.name}, {self.surname}, {self.age})'


class Employee(Person):
    MAX_LVL = 7
    employee_id = ValidateValue('id')

    def __init__(self, lastname: str, name: str, surname: str, age: int, employee_id):
        super().__init__(lastname, name, surname, age)
        self.employee_id = employee_id
        self.level = self.get_level()

    def get_level(self):
        return self.employee_id % self.MAX_LVL

    def __str__(self):
        return (f'{self.lastname} {self.name} {self.surname}. Возраст: {self.age}.\n'
                f'ID: {self.employee_id}\n'
                f'LEVEL: {self.level}')

    def __repr__(self):
        return f'Employee({self.lastname}, {self.name}, {self.surname}, {self.age})'


user_1 = Person('Бирюков', 'Артемий', 'Валерьевич', 30)
user_2 = Employee('Бирюкова', 'Оксана', 'Сергеевна', 29, 787777)
print(user_1)
print(repr(user_1))
print()
print(user_2)
print(repr(user_2))
