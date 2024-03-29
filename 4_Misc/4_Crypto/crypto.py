from itertools import cycle
import re

messagews = input("Enter plain text: ")
key = int(input("Enter shift key: ")) - 1
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

# number of elements as input 
n = int(input("Enter number of shift letters : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = input("Enter alphabet " + str(i+1) +" : " ) 
    app_list.append(ele)

# 
spacel=[]
for i in range(0,len(app_list)):
  num = list_alphabets.index(app_list[i])
  shift_key.append(num)

newlist = [message[i:i + key] for i in range(0, len(message), key)]

new_list=[]
for i in newlist:
  string=i.replace(" ","")
  new_list.append(string)

zip_list = zip(new_list, cycle(app_list))

#last tuple converted to list
last_tuple = list(zip_list[-1])

#last ele in last tuple
lele = last_tuple[-1]


if len(last_tuple[0]) != key:
    del last_tuple[-1]
    del zip_list[-1]
    zip_list.extend(last_tuple)

#converts tuple array to list
res = [''.join(i) for i in zip_list] 
rest=[]

for i in res:
    rest.append(i.lower())

#converts list to string
str1 = ''.join(res)
capital_final = re.sub('([A-Z])', r' \1', str1)
final_string = capital_final.lower()
final_string.strip()
print("Your new shifted text is: " + final_string + "\n")

def find_space(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

space_list = find_space(final_string, " ")
space_list.pop(0)

space_list = [x-1 for x in space_list]
space =[]
for x in range(0,len(space_list)):
    space.append(space_list[x] -x) 

letter_map = {'a': 'h', 'b': 'i', 'c': 'l', 'd': 'w', 'e': 'm', 'f': 'k', 'g': 'b', 'h': 'd', 'i': 'p', 'j': 'c', 'k': 'v', 'l': 'a', 'm': 'z', 'n': 'u', 'o': 's', 'p': 'j', 'q': 'g', 'r': 'r', 's': 'y', 't': 'n', 'u': 'q', 'v': 'x', 'w': 'o', 'x': 'f', 'y': 't', 'z': 'e'}

def subst_cipher(letter_map, text):
    return "".join(letter_map.get(c, " ") for c in text)
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp
def rightrotate(s, d):
    return leftrotate(s, len(s) - d)

#round 1
str1='hilwmkbdpcvazusjgrynqxofte'
first_part=subst_cipher(letter_map, str(rest[0]))
print("Unrotated round is: " + str1)
print("Encrypted part 1 is: " + first_part + "\n")

# all other rotated rounds + substitution with space considered
enc_str=""
for i in range(0,len(shift_key)):
    rot_string = rightrotate(str1, shift_key[i])
    print("Rotated round " + str(i+1) + " is: " + rot_string)
    final_list= [rot_string]
    convert=str(final_list[0])
    lmap=list(convert)
    dictionary = dict(zip(list_alphabets, lmap))
    str_from_res= str(rest[i+1])
    enc_part=subst_cipher(dictionary,str_from_res.replace(" ",""))
    print("Encrypted part " + str(i+2) + " is: " + enc_part + "\n")
    enc_str+=enc_part + " "
    str1= rot_string

enc=first_part + enc_str 
enc = enc.replace(" ","")
d = list(enc)
for index,i in enumerate(space):
    d.insert(index + i, " ")
d = ''.join(d)
print("Your encrypted string is: " + d)