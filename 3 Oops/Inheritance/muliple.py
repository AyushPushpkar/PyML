class Father:
    def skills(self):
        print("Knows driving")

class Mother:
    def traits(self):
        print("Good cook")

class Child(Father, Mother):  # inherits from both
    def hobby(self):
        print("Plays guitar")

c = Child()
c.skills()   # From Father
c.traits()   # From Mother
c.hobby()    # Own method
