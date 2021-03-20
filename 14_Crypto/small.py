def changeWord(word, keyref):
    for letter in word:
        new_letter = chr(keyref + ord(letter))
        word = word.replace(letter, new_letter)
    return word


print(changeWord('hello', 4))