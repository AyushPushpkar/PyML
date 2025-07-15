file = open("write_example.txt", "r")  # Step 1: Open

content = file.read()           # Step 2: Read
print(content)

line = file.readline()     # Reads one line at a time
lines = file.readlines()   # Returns a list of all lines


file.close()                    # Step 3: Close
