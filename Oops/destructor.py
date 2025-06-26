class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        print("File opened")

    def write_data(self, data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print("File closed")

f = FileHandler("example.txt")
f.write_data("Hello, world!")

# When the object `f` is deleted or the program ends, __del__ is called
