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

#Below function calculates factorial of a number
def factorial(n):
   if n == 0:
     return 1
   else:
     N = 1
     for i in range(1, n+1):
       N = N * i
     return(N)

#Below function counts the characters in a word
def count_letters(word, char):
    count = 0
    while count <= len(word):
        for char in word:
            if char == word[count]:
                count += 1
            return count

#Count the number for each character occurence in string and save in dictionary
def counter(input_string):
	dict1={}
	for x in input_string:
	    dict1[x] = dict1.setdefault(x,0)+1
	return dict1

#Function to count most frequent letter in dictionary
def most_frequent_letter(input_dict):
    maximum = 0
    letter_maximum = ""
    for letter in input_dict:
        if input_dict[letter] > maximum:
            maximum = input_dict[letter]
            letter_maximum = letter
    return letter_maximum

#Below function can be used to calculate distance between two points x,y
import math

def distance(x, y):
   distance = math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )
   return distance
x=(0,0)
y=(1,1)
print(distance(x,y))
