class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Object
s1 = Student("Alice", 101)
s1.show()
