# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: Alice
print(person.get("age", 6))  # Output: 25 , If def not provided, it returns None

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Updating a value
person["age"] = 26

# Removing a key-value pair
del person["city"]

person.keys()
person.values()

pair = list(person.items())

# Looping through dictionary
for key, value in person.items():
    print(f"{key}: {value}")


d = dict(name="Alice", age=25)
d2 = dict([("name", "Bob"), ("age", 26)])

print(type(d) )
print(d)
print(type(d2) )
print(d2)

