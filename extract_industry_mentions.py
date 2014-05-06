import sys, re, json, string, functions

import nltk
from nltk.probability import *
from nltk.corpus import stopwords
from nltk.util import bigrams, ngrams

def extract_industry_mentions(text):

	'''
	Set up vars
	'''
	reports = {}
	count = 0
	matches = []

	'''
	Set up some industry lovin'
	'''
	industries = ['education', 'auto', 'b2b', 'beauty', 'beer', 'wine', 'spirits', 'kids', 'entertainment', 'fashion', 'financial', 'fine art', 'food beverage', 'gaming', 'government', 'healthcare', 'health wellness', 'home garden', 'hospitality', 'luxury', 'media', 'multicultural', 'music', 'news', 'non-profit', 'pets', 'pharmaceutical', 'real estate', 'retail', 'small business', 'sports', 'sustainable-green', 'tech', 'mobile', 'travel', 'tourism', 'publishing', 'startup']

	'''
	grab the text input:
	'''
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

	return json.dumps(reports)


if __name__ == '__main__':
	mentions = extract_industry_mentions(sys.argv[1])
	print mentions
