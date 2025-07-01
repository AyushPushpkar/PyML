str1 = "hello, my name is Alice."
str2 = 'She said, "Python is awesome!"'


print(str1 + " " + str2, len(str1))  # Concatenate and print length of str1
print(str2[1:4])  # Slice example
print(str1.endswith("e."))  # True
print(str1.capitalize())  # Capitalizes only the first letter
print(str1.replace("Alice", "Bob"))  # Replaces name
print(str1.find("name"))  # Finds index of substring
print(str1.count("l"))  # Counts how many times 'l' appears


# string[start:stop:step]
print("python"[::-1])

