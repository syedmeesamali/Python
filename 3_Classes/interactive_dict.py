import json

#Below library is for "text processing services"
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('dictionary.json'))

#get_close_matches(word, posibilities, n=3, cutoff=0.66)
#First parameter is of course the word for which you want to find close matches
#Second is a list of sequences against which to match the word
#[optional]Third is maximum number of close matches
#[optional]where to stop considering a word as a match
#(0.99 being the closest to word while 0.0 being otherwise)

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
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        # if answer is yes retrieve the relevant word
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")
    else:
        return ("The word doesn't exist in dictionary")

#input from user
word_user = input("Enter a word: ")

output = retrieve_definition(word_user)

if type(output) == list:
    for item in output:
        print("-", item)
else:
    print("-", output)



