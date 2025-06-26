import os

# File name to delete
file_name = "sample.txt"

# Check if file exists before deleting
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"{file_name} deleted successfully.")
else:
    print(f"{file_name} does not exist.")
