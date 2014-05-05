import sys, re, string, json, functions
import nltk
from nltk.corpus import ieer
from nltk.probability import *


'''
Set up vars
'''
reports = {}

'''
grab the text input:
'''
text = sys.argv[1]

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

print json.dumps(reports)
