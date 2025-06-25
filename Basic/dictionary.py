# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 25

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
