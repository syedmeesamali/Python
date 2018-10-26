def isUpperChar(char):
    if char == char.upper():
        return "True"
    else:
        return "False"


def isUpper(string):
    for c in string:
        if isUpperChar(c) == True:
            print("True")
        else:
            print("False")
        
        
def addToList(x,lst):
    return lst.append(x)
