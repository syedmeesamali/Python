import json
data = json.load(open('dictionary.json'))

#function to retrieve defintion of any word
def retrieve_definition(word):
    if word in data:
        return data[word]
    else:
        return ("The word doesn't exist in dictionary")

#input from user
word_user = input("Enter a word: ")

print(retrieve_definition(word_user))



