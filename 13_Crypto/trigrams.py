import nltk
#nltk.download('webtext')

from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

from nltk.corpus import webtext
textwords = [w.lower() for w in webtext.words('pirates.txt')]

finder = TrigramCollocationFinder.from_words(textwords)
print(finder.nbest(TrigramAssocMeasures.likelihood_ratio, 10))