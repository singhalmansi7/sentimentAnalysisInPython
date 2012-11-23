__author__ = 'msinghal'
import nltk

class Splitter(object):

    def __init__(self):
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def splitParagraphToListOfSentences(self, paragraph):
        sentences = self.nltk_splitter.tokenize(paragraph)
        wordList = [self.nltk_tokenizer.tokenize(sentence) for sentence in sentences]
        return wordList