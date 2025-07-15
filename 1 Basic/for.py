
print("\n== FOR LOOP ==")

# 1. Basic for loop: Print list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 2. Use with break: Stop at 'banana'
for fruit in fruits:
    if fruit == "banana":
        print("Found banana, stopping loop.")
        break
    print(f"Checking: {fruit}")

# 3. Use with continue: Skip 'banana'
for fruit in fruits:
    if fruit == "banana":
        print("Skipping banana")
        continue
    print(f"Kept: {fruit}")

# 4. Use with range()
for i in range(3):
    print(f"Range number: {i}")

# 5. Use with enumerate()
for index, value in enumerate(fruits):
    print(f"Index {index} -> {value}")

# The enumerate() function adds a counter to an iterable (like a list or tuple) and returns it 
# as an enumerate object, which you can loop through.
#enumerate(iterable, start=0)

# 6. Use with else: Run after loop finishes
for i in range(1 , 4):
    print(f"Looping: {i}")
else:
    print("FOR loop completed.")

# 7. Real-world: Mark sheet processing
marks = [80, 45, 92, 33]
for mark in marks:
    if mark < 35:
        print(f"Fail mark found: {mark}")
    else:
        print(f"Passed with: {mark}")
