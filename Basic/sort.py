data = [(1, 3), (4, 1), (2, 2)]

# Using sorted() (returns a new list)
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(4, 1), (2, 2), (1, 3)]

# Or, using .sort() (modifies the list in place)
data.sort(key=lambda x: x[1])
print(data)  # Output: [(4, 1), (2, 2), (1, 3)]


sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
