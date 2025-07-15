# "r" mode: Read-only mode. File must already exist.
# It will raise an error if the file does not exist.
try:
    file = open("sample.txt", "r")
    print("Reading from file (r mode):")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("sample.txt not found!")

# "w" mode: Write mode. Creates a new file or overwrites an existing file.
# WARNING: Existing content will be deleted.
with open("write_example.txt", "w") as file:    # File is automatically closed here
    file.write("This is written using 'w' mode.\n")

# "a" mode: Append mode. Adds to the end of the file, keeps existing content.
with open("write_example.txt", "a") as file:
    file.write("This line is appended using 'a' mode.\n")

# "x" mode: Exclusive creation. Fails if the file already exists.
try:
    with open("new_file.txt", "x") as file:
        file.write("This file was created using 'x' mode.\n")
except FileExistsError:
    print("new_file.txt already exists. 'x' mode cannot overwrite.")

# "b" mode: Binary mode. Used for non-text files (e.g., images, PDFs).
# Combine with "rb", "wb", etc.
with open("binary_file.bin", "wb") as file:
    file.write(b'\xDE\xAD\xBE\xEF')  # Writing binary data

with open("binary_file.bin", "rb") as file:
    content = file.read()
    print("Binary file content (rb mode):", content)

# "t" mode: Text mode. This is the default. Use with "r", "w", etc.
# For example, this is same as open("sample.txt", "rt")
# Default mode doesn't need to specify "t"
