
from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method (no body)

# Concrete Class
class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# animal = Animal()       ❌ Not allowed
dog = Dog()               # ✅ Allowed
cat = Cat()

dog.make_sound()          # Bark!
cat.make_sound()          # Meow!

