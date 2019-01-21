import json
data = json.load(open('dictionary.json'))

#function to retrieve defintion of any word
def retrieve_definition(word):
    #Removing the case-sensitivity from the program
    #For example 'Rain' and 'rain' will give same output
    #Converting all letters to lower because out data is in that format
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return ("The word doesn't exist in dictionary")

#input from user
word_user = input("Enter a word: ")

print(retrieve_definition(word_user))



