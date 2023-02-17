def stringMake():
    final=""
    fileInput = open("input1.txt",'r')
    for line in fileInput:
        line = line.replace("\r","").replace("\n","")
        final = final + " " + str(line)
    print(final)
stringMake()
