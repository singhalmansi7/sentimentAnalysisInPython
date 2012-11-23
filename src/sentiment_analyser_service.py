__author__ = 'msinghal'

from splitter import Splitter
from tagger import POSTagger
from dictionary_tagger import DictionaryTagger

class SentimentAnalyzingService(object):

    def __init__(self):
        self.splitter = Splitter()
        self.postagger = POSTagger()
        self.dicttagger = DictionaryTagger([ '/home/msinghal/PycharmProjects/basic_sentiment_analysis/dicts/positive.yml', '/home/msinghal/PycharmProjects/basic_sentiment_analysis/dicts/negative.yml',
                                    '/home/msinghal/PycharmProjects/basic_sentiment_analysis/dicts/morePositive.yml', '/home/msinghal/PycharmProjects/basic_sentiment_analysis/dicts/moreNegative.yml', '/home/msinghal/PycharmProjects/basic_sentiment_analysis/dicts/invert.yml'])

    def valueOf(self,sentiment):
        if sentiment == 'positive': return 1
        if sentiment == 'negative': return -1
        return 0

    def sentence_score(self,sentence_tokens, previous_token, acum_score):
        if not sentence_tokens:
            return acum_score
        else:
            current_token = sentence_tokens[0]
            tags = current_token[2]
            token_score = sum([self.valueOf(tag) for tag in tags])
            if previous_token is not None:
                previous_tags = previous_token[2]
                if 'inc' in previous_tags:
                    token_score *= 2.0
                elif 'dec' in previous_tags:
                    token_score /= 2.0
                elif 'inv' in previous_tags:
                    token_score *= -1.0
            return self.sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

    def sentiment_score(self,dictTaggedSentences):
        return sum([self.sentence_score(sentence, None, 0.0) for sentence in dictTaggedSentences])

    def performBasicSentimentAnalysis(self, textToBeAnalysed):
        sentences = self.splitter.splitParagraphToListOfSentences(textToBeAnalysed)
        pos_tagged_sentences = self.postagger.pos_tag(sentences)
        dict_tagged_sentences = self.dicttagger.tag(pos_tagged_sentences)

        score = self.sentiment_score(dict_tagged_sentences)
        return  score


