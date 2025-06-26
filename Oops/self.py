# Used to access instance variables inside a class.

class Person:
    def set_name(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

p = Person()
p.set_name("John")
p.show()
