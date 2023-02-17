def Sum1(a,b,c):
    if (a+b+c) == 19:
        return(a+b+c)

def Sum2(a,b,c):
    if (a+b-c) == 10:
        return (a+b-c)

def Sum3(a,b,c):
    if (a-b+c) == 10:
        return (a-b+c)

for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            if Sum1(i,j,k) == True and Sum2(i,j,k) == True and Sum3(i,j,k) == True:
                print("i = ", str(i))
                print("j = ", str(j))
                print("k = ", str(k))
            
    
