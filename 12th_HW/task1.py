# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Если ФИО не соответствует условию, выведите:
#
#
# ФИО должно состоять только из букв и начинаться с заглавной буквы
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
#
#
# Предмет {Название предмета} не найден
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# В противном случае выведите:
#
#
# Оценка должна быть целым числом от 2 до 5
#
# Результат теста должен быть целым числом от 0 до 100
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех
# предметов вместе взятых.
#
# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
#
#
# Математика,Физика,История,Литература
# Создайте класс Student, который будет представлять студента и его успехи по предметам.
# Класс должен иметь следующие методы:
# Атрибуты класса:
#
# name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках
# и результатах тестов для каждого предмета в виде словаря.
#
# Магические методы (Dunder-методы):
#
# __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами.
# Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.
#
# __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name.
# Убеждается, что name начинается с заглавной буквы и состоит только из букв.
#
# __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.
#
# __str__(self): Возвращает строковое представление студента, включая имя и список предметов.
# Студент: Иван Иванов
# Предметы: Математика, История
#
# Методы класса:
#
# load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла
# и добавляет предметы в атрибут subjects.
#
# add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
# Убеждается, что оценка является целым числом от 2 до 5.
#
# add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету.
# Убеждается, что результат теста является целым числом от 0 до 100.
#
# get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
#
# get_average_grade(self): Возвращает средний балл по всем предметам.
import csv


class NameDescriptor:
    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate_name(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate_name(self, value):
        if not value.istitle() or not (isinstance(i, str) for i in value):
            raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Student:
    name = NameDescriptor()

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        data = {}
        with open(subjects_file, 'r', encoding="UTF-8") as file:
            subjects_file = file.read()
            for i in subjects_file.split(','):
                data[i] = {'grade': [], 'test_score': []}
        return data

    def __str__(self):
        subjects_str = ''
        for key in self.subjects.keys():
            if len(self.subjects[str(key)]['grade']) != 0 or len(self.subjects[str(key)]['test_score']) != 0:
                subjects_str += key + ', '
        return (f'Студент: {self.name}\n'
                f'Предметы: {subjects_str[:-2]}')

    def add_grade(self, subject, grade: int):
        self.validate_subject(subject)
        self.validate_grade(grade)
        self.subjects[subject]['grade'].append(grade)

    def add_test_score(self, subject, test_score):
        self.validate_subject(subject)
        self.validate_test_score(test_score)
        self.subjects[subject]['test_score'].append(test_score)

    def get_average_test_score(self, subject):
        self.validate_subject(subject)
        sum_score = 0
        for i in self.subjects[subject]['test_score']:
            sum_score += i
        return sum_score / len(self.subjects[subject]['test_score'])

    def get_average_grade(self):
        count_grades = 0
        sum_grade = 0
        for value in self.subjects.values():
            for grade in value['grade']:
                sum_grade += grade
            count_grades += len(value['grade'])
        return sum_grade / count_grades

    def validate_subject(self, subject):
        if subject not in self.subjects.keys():
            raise ValueError(f'Предмет {subject} не найден')

    def validate_grade(self, grade):
        if not isinstance(grade, int) or not 2 <= grade <= 5:
            raise ValueError(f'Оценка должна быть целым числом от 2 до 5')

    def validate_test_score(self, test_score):
        if not isinstance(test_score, int) or not 0 <= test_score <= 100:
            raise ValueError(f'Результат теста должен быть целым числом от 0 до 100')
