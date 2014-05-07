import sys, re, json, string, functions

import nltk
from nltk.probability import *
from nltk.corpus import stopwords
from nltk.util import bigrams, ngrams

'''
Set up vars
'''
reports = {}
count = 0
matches = []

'''
Set up some industry lovin'
'''
industries = {
	'education': 'education',
	'auto': 'auto',
	'b2b', 'beauty': 'beauty',
	'beer': 'beer-wine-spirits',
	'wine': 'beer-wine-spirits',
	'spirits': 'beer-wine-spirits',
	'kids': 'kids',
	'children': 'kids',
	'entertainment': 'entertainment',
	'celebrity': 'entertainment',
	'celebrities': 'entertainment',
	'fashion': 'fashion',
	'financial': 'financial',
	'investment': 'financial',
	'bank': 'financial',
	'fine art': 'fine art',
	'food beverage': 'food-beverage',
	'gaming': 'gaming',
	'government': 'government',
	'healthcare': 'healthcare',
	'health': 'health-wellness',
	'wellness': 'health-wellness',
	'home garden': 'home-garden',
	'hospitality': 'hospitality',
	'hotel': 'hospitality',
	'hotels': 'hospitality',
	'luxury': 'luxury',
	'media': 'media',
	'multicultural': 'multicultural',
	'music': 'music',
	'news': 'news',
	'non-profit': 'non-profit',
	'pets': 'pets',
	'pharmaceutical': 'pharmaceutical',
	'real estate': 'real-estate',
	'retail': 'retail',
	'small business': 'small-business',
	'smb': 'small-business',
	'small medium size business': 'small-business',
	'sports': 'sports',
	'sustainable-green': 'sustainable-green',
	'tech': 'tech-it',
	'tech': 'tech-it',
	'software development': 'tech-it',
	'consumer electronics': 'tech-it',
	'mobile': 'mobile',
	'travel': 'travel',
	'tourism': 'tourism',
	'publishing': 'publishing',
	'startup': 'startup',
}

'''
grab the text input:
'''
text = sys.argv[1]
text = text.replace('\n', ' ')
text = text.lower().strip()

'''
tokenize and bigram
'''
tk_text = functions._word_tokenize(text)
bigrams_all = nltk.bigrams(tk_text)

'''
Find Industry Mentions in Bigrams
'''
for bigram_dict in bigrams_all:
	bigram = bigram_dict[0] + ' ' + bigram_dict[1]
	if bigram in industries:
		matches.append(bigram)
		count += 1
		#remove to keep single word counts clean:
		text = text.replace(bigram, '')

'''
Find Industry Mentions in remaining words:
'''
words = text.split()
for word in words:
	if word in industries:
		matches.append(word)
		count += 1

'''
Assemble the final output:
'''
for match in matches:
	if match in reports:
		reports[match] += 1
	else:
		reports[match] = 1

print json.dumps(reports)