from abc import ABC, abstractmethod

class Animal(ABC):
    def init(self, name):
        self._name = name  

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):  
        return self._name

class Dog(Animal):
    def init(self, name, breed):
        super().init(name)  
        self._breed = breed  

    def make_sound(self):
        return "Woof!"

    def get_breed(self):  
        return self._breed

class Cat(Animal):
    def init(self, name, color):
        super().init(name)  
        self._color = color  

    def make_sound(self): 
        return "Meow!"

    def get_color(self):
        return self._color

dog = Dog("Rex", "German Shepherd")
print(dog.get_name(), "is a", dog.get_breed(), "and says", dog.make_sound())

cat = Cat("Mittens", "Black")
print(cat.get_name(), "is a", cat.get_color(), "cat and says", cat.make_sound())