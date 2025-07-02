
def check():
    word = "append"
    data = True
    line = 1 

    with open("write_example.txt" , "r") as f :
        while data :
            data = f.readline()
            if(word in data) :
                print(line)
                return
            line+= 1

    return -1

check()