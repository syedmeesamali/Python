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

print(subst_cipher(letter_map, "green"))