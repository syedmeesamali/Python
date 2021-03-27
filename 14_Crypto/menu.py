from itertools import cycle
import re
import sys
import string
from termcolor import colored, cprint

print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')

def encrypt():
    messagews = input("Enter plain text: ")
    key = int(input("Enter shift key: "))-1
    list_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z']
    p_string = str(messagews)
    app_list = []
    shift_key = []
    split = p_string.split()
    split = [i.capitalize() for i in split]
    print(split)
    lenlist = []
    for x in split:
        lenlist.append(len(x))
    message = ""
    for i in split:
        message += i
    # number of elements as input 
    n = int(input("Enter number of shift letters : "))

    for i in range(0, n): 
        ele = input("Enter alphabet " + str(i+1) +": " )
        app_list.append(ele)

    #----------------------------------------------------------------------------
    ''' Zip to cycle and add additonal letter to plain text'''
    newlist = [message[i:i + key] for i in range(0, len(message), key)]
    new_list = []   #List to hold chars without spaces
    for i in newlist:
        string = i.replace(" ","")
        new_list.append(string)
    zip_list = zip(new_list, cycle(app_list))
    zipped = list(zip_list)
    print("hi")
    print(str(zipped))
    '''last_tuple = zipped[-1]
    list_last_tuple = list(last_tuple)
    lele = last_tuple[-1]
    if len(last_tuple[0]) != key:
        zipped.extend(list_last_tuple)'''
    #------------------------------------------------------------------------------
    ''' rep for making length of additional letters list for subst for loop'''
    rep=[]
    mod = int(len(zipped)/len(app_list))
    for x in range(0,mod):
      for y in range(0,len(app_list)):
        rep.append(app_list[y])
    print("rep")
    print (rep)
    shift_keys=[]
    for i in range(0, len(rep)):
        num = list_alphabets.index(rep[i])
        shift_keys.append(num)
    print(shift_keys)
    #----------------------------------------------------------------------
    ''' space preservation by capitalizing the first letter of each word and displaying the final shifted string message'''
    print(zipped)
    print (len(zipped))
    res = [''.join(i) for i in zipped]
    print("res here")
    print(res)
    rest =[]
    for i in res:
        rest.append(i.lower())      #Lower letters all saved in list ----- rest[]
    str1 = ''.join(res)     #converts list to string
    print("str1: " + str1)
    capital_final = re.sub('([A-Z])', r' \1', str1)
    final_string = capital_final.lower()
    final_string.strip()
    def find_space(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]
    space_list = find_space(final_string, " ")
    #space_list.pop(0)
    print("Your new shifted text is: " + final_string + "\n")
    space_list = [x-1 for x in space_list]
    space =[]
    for x in range(0, len(space_list)):
        space.append(space_list[x] -x)

#----------------------------------------------------------------------------
    ''' ENCRYPTION STARTS HERE'''

    letter_map = {'a': 'h', 'b': 'i', 'c': 'l', 'd': 'w', 'e': 'm', 'f': 'k', 'g': 'b', 'h': 'd', 'i': 'p', 
    'j': 'c', 'k': 'v', 'l': 'a', 'm': 'z', 'n': 'u', 'o': 's', 'p': 'j', 'q': 'g', 'r': 'r', 's': 'y', 't': 'n', 
    'u': 'q', 'v': 'x', 'w': 'o', 'x': 'f', 'y': 't', 'z': 'e'}
    def subst_cipher(letter_map, text):
        return "".join(letter_map.get(c, " ") for c in text)
    def leftrotate(s, d):
        tmp = s[d : ] + s[0 : d]
        return tmp
    def rightrotate(s, d):
        return leftrotate(s, len(s) - d)

    str1='hilwmkbdpcvazusjgrynqxofte'
    first_part = subst_cipher(letter_map, str(rest[0]))
    print("Unrotated round is: " + str1)
    print("Encrypted part 1 is: " + first_part + "\n")

    enc_str = ""
    for i in range(0, len(shift_keys)):
        j = 0
        while(j < len(shift_keys)):
            rot_string = rightrotate(str1, shift_keys[i])
            j = j + 1
        print("Rotated round " + str(i+1) + " is: " + rot_string)    
        final_list= [rot_string]
        convert = str(final_list[0])
        lmap = list(convert)
        dictionary = dict(zip(list_alphabets, lmap))
        try:
            str_from_res= str(rest[i+1])
        except:
            pass
        print(str_from_res)
        enc_part = subst_cipher(dictionary,str_from_res.replace(" ",""))
        print("Encrypted part " + str(i+2) + " is: " + enc_part + "\n")
        enc_str += enc_part + " "
        str1 = rot_string

    enc = first_part + enc_str 
    enc = enc.replace(" ","")
    print(enc)
    d = list(enc)
    for index,i in enumerate(space):
        d.insert(index + i, " ")

    d = ''.join(d)
    print("Your encrypted string is: " + d)

#--------------------------------------------------------------------

def decrypt():
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
    #------------------------------------------------------------------------
    '''' preserving space for final decrypted text '''
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

    #------------------------------------------------------------------------
    ''' Removing the extra letters from cipher text '''
    def replace_n(string_val, n, first=0):
        letters = (
            " " if i % n == 0 else char
            for i, char in enumerate(string_val, -first)
        )
        return ''.join(letters)
    cstring = replace_n(without_space, key+1, first=-1)
    clist = list(map(str, cstring.split(' ')))
    print(clist)
    new_list=[]
    for i in new_list:
      string=i.replace(" ","")
      new_list.append(string)
    lower_list=[]
    for i in new_list:
        lower_list.append(i.lower())
    #--------------------------------------------------------------------------
    ''' Getting the shift keys and rotation list for subst function'''
    rep=[]
    mod = int(len(clist)/len(app_list))
    for x in range(0,mod):
      for y in range(0,len(app_list)):
        rep.append(app_list[y])
    print("rep")
    print (rep)
    shift_keys=[]
    for i in range(0, len(rep)):
        num = list_alphabets.index(rep[i])
        shift_keys.append(num)
    print(shift_keys)
    # ------------------------------------------------------------------------
    ''' DECRYPTION STARTS HERE'''
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
    for i in range(0,len(shift_keys)):
      j = 0
      while(j < len(clist) ):
        rot_string = rightrotate(str1, shift_keys[i])
        j = j + 1
      print("Rotated round " + str(i+1) + " is: " + rot_string)  
      final_list= [rot_string]
      convert=str(final_list[0])
      lmap=list(convert)
      dictionary1 = dict(zip(lmap,list_alphabets))
      str_from_res= str(clist[i+1])
      dec_part=subst_cipher(dictionary1,str_from_res)
      print("Decrypted part " + str(i+2) + " is: " + dec_part + "\n")
      dec_str+=dec_part + " "
      str1= rot_string
      
    dec=first_part + dec_str 
    d = dec.replace(" ","")
    d = list(d)
    for index,i in enumerate(space):
        d.insert(index + i, " ")
    d = ''.join(d)
    print("The decrypted text is: "+ d)
    print("\n")

def print_menu():  ## Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("Choose option 1 to encrypt a plaintext message")
    print("Choose option 2 to decrypt a cipher message")
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Exit")
    print(67 * "-")

loop = True
while loop:
    print_menu()
    choice = input("Enter your choice [1-3]: ")

    if choice == '1':
        print_green("Encryption option has been selected")
        print("The algorithm takes 3 user inputs:")
        print("    1. Plaintext message")
        print("    2. Shift key which determines  the position at which the shift letter added.")
        print("    3. Number of shift letters: This is the additional letters added to the plain text to make the encryption stronger.")
        print("    4. Shift letters: Next you are prompted to enter your shift letters, for example if your number of shift letters is 2, you can input any two alphabets like a and b, which are added to the position of your ""shift key"" number. "  
         )
        encrypt()
    elif choice == '2':
        print_green("Decryption option has been selected")
        print("The algorithm takes 3 user inputs:")
        print("    1. Ciphertext message")
        print("    2. Shift key which determines the rotation of the alphabets used for substituion of letters to produce cipher text.")
        print("    3. Number of shift letters: this determines the quantity of the shift letters to be appended at the shift key's index, which append via a cycle of each letter.")
        print("    4. Shift letters: the shift letters chosen (alphabetical characters) that will be cycled and appended at the shift keys' indeces.")
        decrypt()
    elif choice == '3':
        loop = False