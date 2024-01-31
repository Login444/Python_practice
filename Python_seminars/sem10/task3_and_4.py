# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Human:
    def __init__(self, lastname, name, surname, age, city):
        self.name = name
        self.lastname = lastname
        self.surname = surname
        self._age = age
        self.city = city

    def birthday(self):
        self._age += 1
        print(f'Happy {self._age}')

    def full_name(self):
        print(f'{self.lastname} {self.name} {self.surname}')


me = Human('Бирюков', 'Артемий', 'Валерьевич', 29, 'Москва')
me.birthday()
me.full_name()


# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь


class Worker(Human):
    def __init__(self, u_id, lastname, name, surname, age, city):
        super().__init__(lastname, name, surname, age, city)
        if len(str(u_id)) < 6:
            self.u_id = str(u_id).zfill(6)
        elif len(str(u_id)) > 6:
            self.u_id = str(u_id)[:6]
        else:
            self.u_id = str(u_id)
        self.u_lvl = self.__lvl()

    def __lvl(self):
        return sum(int(i) for i in self.u_id) % 7


worker1 = Worker(123456, 'Бирюков1', 'Артемий', 'Валерьевич', 29, 'Москва')
worker2 = Worker(12345, 'Бирюков2', 'Артемий', 'Валерьевич', 29, 'Москва')
worker3 = Worker(2334567, 'Бирюков3', 'Артемий', 'Валерьевич', 29, 'Москва')

print(f'{worker1.lastname = }, {worker1.u_id = }, {worker1.u_lvl = }')
print(f'{worker2.lastname = }, {worker2.u_id = }, {worker2.u_lvl = }')
print(f'{worker3.lastname = }, {worker3.u_id = }, {worker3.u_lvl = }')
