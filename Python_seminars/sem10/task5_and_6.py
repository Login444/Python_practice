# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('Животина')


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type

    # def info(self):
    #     print(f'Я рыба {self.name},мне {self.age} лет, плаваю в {self.water_type}')


class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def info(self):
        print(f'Я птица {self.name},мне {self.age} лет, цвет - {self.color}')


class Horse(Animal):
    def __init__(self, name, age, hooves):
        super().__init__(name, age)
        self.hooves = hooves

    def info(self):
        print(f'Я лошадь {self.name},мне {self.age} лет, у меня {self.hooves} копыта')


horse = Horse('Jack', 15, 4)
bird = Bird('John', 5, 'red')
fish = Fish('Nemo', 1, 'sea')

horse.info()
bird.info()
fish.info()
