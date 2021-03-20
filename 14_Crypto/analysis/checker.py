import enchant
from enchant.checker import SpellChecker
import re
import sys
import string
d = enchant.Dict("en_US")

messagews = "brmmu lhrm wos fhhc efesefset ctk qymdzv"
split_text = messagews.split()
#split = [i.capitalize() for i in split_text]
ourlist=[]
for x in split_text:
    ourlist.append(x)
print(ourlist)

letter_map = {'h': 'a', 'i': 'b', 'l': 'c', 'w': 'd', 'm': 'e', 'k': 'f', 'b': 'g', 'd': 'h', 
'p': 'i', 'c': 'j', 'v': 'k', 'a': 'l', 'z': 'm', 'u': 'n', 's': 'o', 'j': 'p', 'g': 'q', 
'r': 'r', 'y': 's', 'n': 't', 'q': 'u', 'x': 'v', 'o': 'w', 'f': 'x', 't': 'y', 'e': 'z'}

''' 3 functions for substituion and rotation of letter map'''
def subst_cipher(letter_map, text):
    return "".join(letter_map.get(c, "") for c in text)

str1='hilwmkbdpcvazusjgrynqxofte'
cipher_list = []
for element in ourlist:
    cipher_list.append(subst_cipher(letter_map, element))

print(cipher_list)
final_list = []
result_list = []
for x in cipher_list:
    if (d.check(x) != True):
        final_list.append(x)
    else:
        result_list.append(x)

print(final_list)
ref_list = []

def shift(s, n):
    return ''.join(chr((ord(char) - 97 + n) % 26 + 97) for char in s)

def changeWord(word, keyref):
    for letter in word:
        new_letter = chr(keyref + ord(letter))
        word = word.replace(letter, new_letter)
    return word

n = int(input("Enter number of shift letters (0 to Exit)"))
count = 0
while(n != 0):
    count += 1
    ref_list = []
    print(f"Shift # {count} is: " + str(n))
    for ele in final_list:
        ref_list.append(shift(ele, n))
    print(ref_list)
    n = int(input("Enter number of shift letters (0 to Exit)"))

result_list.append(ref_list)
print("Final list is:")
print(" ".join(word[0] for word in ref_list))