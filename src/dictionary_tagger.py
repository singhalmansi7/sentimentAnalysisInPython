__author__ = 'msinghal'

import yaml

class DictionaryTagger(object):

    def __init__(self, filePaths):
        files = [open(path, 'r') for path in filePaths]
        dictionaries = [yaml.load(file) for file in files]
        map(lambda x: x.close(), files)
        self.dictionary = {}
        self.max_key_size = 0
        for dictionary in dictionaries:
            for key in dictionary:
                self.dictionary[key] = dictionary[key]
                self.max_key_size = max(self.max_key_size, len(key))

    def tag(self, postagged_sentences):
        return [self.tag_sentence(sentence) for sentence in postagged_sentences]

    def tag_sentence(self, sentence, tagWithLemmas=False):
        tag_sentence = []
        sentenceLength = len(sentence)
        if self.max_key_size == 0:
            self.max_key_size = sentenceLength
        startPositionOfSentence = 0
        while (startPositionOfSentence < sentenceLength):
            EndPositionOfSentence = min(startPositionOfSentence + self.max_key_size, sentenceLength)
            tagged = False
            while (EndPositionOfSentence > startPositionOfSentence):
                expression_form = ' '.join([word[0] for word in sentence[startPositionOfSentence:EndPositionOfSentence]]).lower()
                expression_lemma = ' '.join([word[1] for word in sentence[startPositionOfSentence:EndPositionOfSentence]]).lower()
                if tagWithLemmas:
                    literal = expression_lemma
                else:
                    literal = expression_form
                if literal in self.dictionary:
                    is_single_token = EndPositionOfSentence - startPositionOfSentence == 1
                    original_position = startPositionOfSentence
                    startPositionOfSentence = EndPositionOfSentence
                    taggings = [tag for tag in self.dictionary[literal]]
                    tagged_expression = (expression_form, expression_lemma, taggings)
                    if is_single_token:
                        original_token_tagging = sentence[original_position][2]
                        tagged_expression[2].extend(original_token_tagging)
                    tag_sentence.append(tagged_expression)
                    tagged = True
                else:
                    EndPositionOfSentence = EndPositionOfSentence - 1
            if not tagged:
                tag_sentence.append(sentence[startPositionOfSentence])
                startPositionOfSentence += 1
        return tag_sentence
