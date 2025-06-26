class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def greet(cls):
        print("Welcome to Math class")

print(Math.add(5, 3))  # 8
Math.greet()


#  1. @staticmethod
# Belongs to the class, but doesn't know anything about the class or instance.
# It doesn’t take self or cls as a parameter.
# Used when the method doesn’t need to access class or instance data.