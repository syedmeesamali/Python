import nltk, collections
from nltk.corpus import webtext
from nltk.collections import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures


textwords = [w.lower() for w in webtext.words('pirates.txt')]
finder = BigramCollocationFinder.from_words(textwords)
finder.nbest(BigramAssocMeasures.likelihood_ratio, 10)