__author__ = 'msinghal'
import nltk

class POSTagger(object):

    def __init__(self):
        pass

    def pos_tag(self, listOfSentences):
        taggedSentences = [nltk.pos_tag(sentence) for sentence in listOfSentences]
        taggedWords = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in taggedSentences]
        return taggedWords
