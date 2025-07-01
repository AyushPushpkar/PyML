class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

    def wag_tail(self):
        print("Dog wags tail")

# Parent pointer pointing to child object
a: Animal = Dog()

a.speak()        # ✅ Calls Dog's overridden method → "Dog barks"
# a.wag_tail()   # ❌ Error: Animal reference doesn't know wag_tail()

# Safe way to access child-only methods
if isinstance(a, Dog):
    a.wag_tail()  # ✅ Works

c = Animal()
d = Dog()

c.speak()
d.speak()
