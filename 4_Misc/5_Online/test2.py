p = False
q = True
#print(not (p or not q))

bool1 = True
bool2 = False
#print(not False)
#print(bool1 != False)
#print(not (bool1 == bool2))

def nand(bool1, bool2):
    """
    Take two Boolean values bool1 and bool2
    and return the specified Boolean values
    """   
    if bool1:
        if bool2:
            return False
        else:
            return True
    else:
        return True

print(nand(bool1, bool2))
print(not (bool1 or bool2))
print(not(bool1 and bool2))