import sys, re, string, json, functions
import nltk
from nltk.corpus import ieer
from nltk.probability import *

'''
Set up stopwords
'''
from nltk.corpus import stopwords
stop = stopwords.words('english')

'''
Set up vars
'''
reports = {}
companies = {}
company = {}
matches = {}


'''
grab the text input:
'''
text = sys.argv[1]

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

print json.dumps(entity_names)
