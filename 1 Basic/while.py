

# 1. Basic while loop: Count from 1 to 5
i = 1
while i <= 5:
    print(f"Count: {i}")
    i += 1

# 2. Use with break: Stop at 3
i = 1
while i <= 5:
    if i == 3:
        print("Breaking at 3")
        break
    print(f"Value: {i}")
    i += 1

# 3. Use with continue: Skip 3
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping 3")
        continue
    print(f"Looping: {i}")

# 4. Use with else: Print when loop ends normally
i = 1
while i <= 3:
    print(f"Normal loop: {i}")
    i += 1
else:
    print("Loop completed successfully.")

# 5. Real-world: password retry
attempts = 0
password = ""
while password != "1234" and attempts < 3:
    password = input("Enter password: ")
    attempts += 1
    if password == "1234":
        print("Access granted.")
        break
else:
    print("Too many attempts. Access denied.")
