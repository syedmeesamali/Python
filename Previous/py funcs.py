#Simple function to add numbers
def add(a,b):
    mysum = a + b
    return mysum

#Function to find intersection of two lists
def intersect(s1,s2):
    #res is empty list to store numbers
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res
    
#Function to create random password from a given length and characters saved
import random
def password(length):
    #pw is empty string to later store password
    pw = str()
    chars = "abcdefghijklmn"
    for i in range(length):
        pw = pw + random.choice(chars)
    return pw

def factorial(n):
   if n == 0:
     return 1
   else:
     N = 1
     for i in range(1, n+1):
       N = N * i
     return(N)
