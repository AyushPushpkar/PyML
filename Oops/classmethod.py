class Pizza:
    base_price = 100  # class variable

    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def veg(cls):
        return cls(['tomato', 'onion'])  # returns an instance

    @classmethod
    def get_base_price(cls):
        return cls.base_price

p = Pizza.veg()
print(p.toppings)  # ['tomato', 'onion']
print(Pizza.get_base_price())  # 100

# | Keyword | Refers To                              | Used In          | Purpose                                                                |
# | ------- | -------------------------------------- | ---------------- | ---------------------------------------------------------------------- |
# | `self`  | The **instance** of the class (object) | Instance methods | To access or modify **object-level (instance)** variables and methods  |
# | `cls`   | The **class itself**                   | Class methods    | To access or modify **class-level** variables and create new instances |

