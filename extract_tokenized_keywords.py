import sys, re, string, json, functions
import nltk
from nltk.corpus import ieer
from nltk.probability import *

def extract_tokenized_keywords(text):

    '''
    Set up vars
    '''
    reports = {}

    '''
    pre-process
    '''
    tk_text = text.replace('\n', ' ')
    tk_text = nltk.clean_html(tk_text.strip().lower())

    #regular methods:
    tokens = nltk.word_tokenize(tk_text)
    tokens = functions._remove_stop_words(tokens)
    stems = functions._stem(tokens)

    for stem in stems:
        if stem in reports:
            reports[stem] += 1
        else:
            reports[stem] = 1

    return json.dumps(reports)


if __name__ == '__main__':
    keywords = extract_tokenized_keywords(sys.argv[1])
    print keywords
