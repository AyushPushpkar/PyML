
def check():
    word = "boss"
    data = True
    line = 1 

    with open("samle" , "r") as f :
        while data :
            data = f.readline()
            if(word in data) :
                print(line)
                return
            line+= 1

    return -1

check()