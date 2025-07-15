# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)
len(fruits)

# Adding an element
fruits.add("orange")
print(fruits)

# Updating a set with multiple items
fruits.update(["mango", "grape"])
print(fruits)

# Removing an element (raises error if not found)
fruits.remove("banana")

# Discarding an element (no error if not found)
fruits.discard("pineapple")

# Popping a random item
removed_item = fruits.pop()
print(f"Removed: {removed_item}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))         # {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # {3}
print(set1.difference(set2))    # {1, 2}
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}

# Checking membership
print("apple" in fruits)

# Clearing a set
fruits.clear()
print(fruits)  # Output: set()

null = set()