class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):  # 1st level
    def bark(self):
        print("Dog barks")

class Puppy(Dog):   # 2nd level
    def play(self):
        print("Puppy plays")

p = Puppy()
p.move()   # From Animal
p.bark()   # From Dog
p.play()   # From Puppy
