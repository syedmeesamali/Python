import re
import sys
import string
from termcolor import colored

# Getting cipher text and input validation
messagews = input("Enter ciphertext: ")
if all(x.isalpha() or x.isspace() for x in messagews):
    pass
else:
    print("Enter only alphabetical letters and spaces")
    sys.exit()
try:
  key = int(input("Enter shift key: "))-1
except ValueError:
    print("Please input integer only") 
    sys.exit()
# declaring variables
list_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
p_string = str(messagews)
app_list = []
shift_key = []
split = p_string.split()
split = [i.capitalize() for i in split]
lenlist=[]
for x in split:
    lenlist.append(len(x))
message=""
for i in split:
  message+=i
# Getting shift letters and input validation
try:
    # number of elements as input 
    n = int(input("Enter number of shift letters : "))
except ValueError and NameError:
    print("Please input integer only") 
    sys.exit()
# iterating till the loop till shift letters
for i in range(0, n): 
    ele = input("Enter alphabet " + str(i+1) +" : " ) 
    if len(ele) == 1:
        if ele in string.ascii_letters:
            pass
        else:
            print('Please enter only letters')
            sys.exit()
    else:
        print('Please enter only one character')
        sys.exit()
    app_list.append(ele)
print("\n")
# getting alphabet numbers for shift letters  
for i in range(0,len(app_list)):
  num = list_alphabets.index(app_list[i])
  shift_key.append(num)

# preserving space for final decrypted text
def find_space(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
space_list = find_space(messagews, " ")
without_space=messagews.replace(" ","")

# getting index of spaces
capital_final = re.sub('([A-Z])', r' \1', messagews)
final_string = capital_final.lower()
final_string.strip()

space_list = [x-1 for x in space_list]
space =[]
for x in range(0,len(space_list)):
    space.append(space_list[x] -x)

# removing the extra letters 
def replace_n(string_val, n, first=0):
    letters = (
        " " if i % n == 0 else char
        for i, char in enumerate(string_val, -first)
    )
    return ''.join(letters)
cstring = replace_n(without_space, key+1, first=-1)

# ---------------------------------
clist = list(map(str, cstring.split(' ')))
print(clist)
new_list=[]
for i in new_list:
  string=i.replace(" ","")
  new_list.append(string)
lower_list=[]
for i in new_list:
    lower_list.append(i.lower())
# -------------------------------
letter_map = {'h': 'a', 'i': 'b', 'l': 'c', 'w': 'd', 'm': 'e', 'k': 'f', 'b': 'g', 'd': 'h', 
'p': 'i', 'c': 'j', 'v': 'k', 'a': 'l', 'z': 'm', 'u': 'n', 's': 'o', 'j': 'p', 'g': 'q', 
'r': 'r', 'y': 's', 'n': 't', 'q': 'u', 'x': 'v', 'o': 'w', 'f': 'x', 't': 'y', 'e': 'z'}
def subst_cipher(letter_map, text):
    return "".join(letter_map.get(c, " ") for c in text)
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp
def rightrotate(s, d):
    return leftrotate(s, len(s) - d)

#round 1
str1='hilwmkbdpcvazusjgrynqxofte'
first_part=subst_cipher(letter_map, str(clist[0]))
print("Unrotated round is: " + str1)
print("Decrypted part 1 is: " + first_part + "\n")

# all other rotated rounds + substitution with space considered
dec_str=""
for i in range(0, len(clist)-1):
  j = 0
  while(j < len(clist)):
    rot_string = rightrotate(str1, shift_key[i])
    j = j + 1
  print("Rotated round " + str(i+1) + " is: " + rot_string)  
  final_list= [rot_string]
  convert = str(final_list[0])
  lmap = list(convert)
  dictionary1 = dict(zip(lmap,list_alphabets))
  try:
    str_from_res= str(clist[i+1])
  except:
    pass
  dec_part = subst_cipher(dictionary1,str_from_res)
  print("Decrypted part " + str(i+2) + " is: " + dec_part + "\n")
  dec_str += dec_part + " "
  str1 = rot_string
  
dec = first_part + dec_str 
d = dec.replace(" ","")
d = list(d)
for index,i in enumerate(space):
    d.insert(index + i, " ")
d = ''.join(d)
print("The decrypted text is: "+ d)