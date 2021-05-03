string = 'this is a simple string to check for the word frequencies in text'

list_words = string.split()
freq = []
for w in list_words:
    freq.append(list_words.count(w))

print('String is: \n' + string)
print('List is: ' + str(list_words) + '\n')
print('Frequency is: ' + str(freq) + '\n')
print('Pairs: \n' + str(list(zip(list_words, freq))))


def wordListToDict(wordList):
    wordfreq = [wordList.count(p) for p in wordList]
    return dict(list(zip(wordList, wordfreq)))

print(wordListToDict(list(string)))

