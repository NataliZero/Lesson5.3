# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def eat(self):
        print(f"{self.name} is eating.")

# Подкласс Bird (Птицы)
class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly  # Специфический атрибут для птиц, могут ли они летать

    def make_sound(self):
        print(f"{self.name} chirps.")  # Переопределённый метод для птиц

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying.")
        else:
            print(f"{self.name} cannot fly.")

# Подкласс Mammal (Млекопитающие)
class Mammal(Animal):
    def __init__(self, name, age, has_fur):
        super().__init__(name, age)
        self.has_fur = has_fur  # Специфический атрибут для млекопитающих, есть ли у них шерсть

    def make_sound(self):
        print(f"{self.name} makes mammal sound.")  # Переопределённый метод для млекопитающих

    def show_fur(self):
        if self.has_fur:
            print(f"{self.name} has fur.")
        else:
            print(f"{self.name} does not have fur.")

# Подкласс Reptile (Пресмыкающиеся)
class Reptile(Animal):
    def __init__(self, name, age, is_cold_blooded):
        super().__init__(name, age)
        self.is_cold_blooded = is_cold_blooded  # Специфический атрибут для пресмыкающихся (холоднокровные или нет)

    def make_sound(self):
        print(f"{self.name} hisses.")  # Переопределённый метод для пресмыкающихся

    def show_temperature_regulation(self):
        if self.is_cold_blooded:
            print(f"{self.name} is cold-blooded.")
        else:
            print(f"{self.name} is not cold-blooded.")

# Функция для демонстрации полиморфизма
def animal_sound(animal_list):
    for animal in animal_list:
        animal.make_sound()

# Создадим объекты разных животных
parrot = Bird("Parrot", 2, can_fly=True)
elephant = Mammal("Elephant", 10, has_fur=False)
snake = Reptile("Snake", 4, is_cold_blooded=True)

# Создадим список животных
animals = [parrot, elephant, snake]

# Вызовем функцию, которая продемонстрирует полиморфизм
animal_sound(animals)

