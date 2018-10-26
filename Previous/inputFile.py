def main():
    myList = []
    newList = []
    fileInput = open("input.txt",'r')
    for line in fileInput:
        line = line.replace("\r","").replace("\n","")
        myList.append(line)
    print(myList)
main()

def find_min_val(lst):
    mini = lst[0]
    for i in range(len(lst)-1):
        if mini < lst[i]:
            mini = lst[i]
    return mini


