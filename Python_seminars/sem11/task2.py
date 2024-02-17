# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    archive = []

    def __new__(cls, letter, digit):
        instance = super().__new__(cls)
        instance.digit = digit
        instance.letter = letter
        instance.archive = cls.archive.copy()
        cls.archive.append(instance)
        return instance

    def __str__(self):
        return f'Объект архив({self.digit}, {self.letter}). Архив: {self.archive}'

    def __repr__(self):
        return f'{self.digit} {self.letter}'


a = Archive('A', 1)
b = Archive('B', 2)
c = Archive('C', 3)
d = Archive('D', 4)

print(a)
print(b)
print(c)
print(d)
