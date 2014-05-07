import sys, re, string, json, functions
import nltk
from nltk.corpus import ieer, stopwords
from nltk.probability import *


def extract_named_entities(text):

    '''
    Set up stopwords
    '''
    stop = stopwords.words('english')

    '''
    Set up vars
    '''
    reports = {}
    companies = {}
    company = {}
    matches = {}

    '''
    pre-process
    '''
    tk_text = text.replace('\n', ' ')
    tk_text =  nltk.clean_html(tk_text.strip())

    #regular methods:
    sentences = nltk.sent_tokenize(tk_text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=False)


    entity_names = {}

    for tree in chunked_sentences:

        #extract named entities:
        ents = functions.extract_entity_names(tree)

        if ents:
            #increment occurrence or add to dict:
            if ents['ne'] in entity_names:
                entity_names[ents['ne']]['count'] += 1
            else:
                entity_names[ents['ne']] = { 'type': ents['type'], 'count': 1}

    return json.dumps(entity_names)


if __name__ == '__main__':
    names = extract_named_entities(sys.argv[1])
    print names
