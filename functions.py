import nltk
from nltk.probability import *
from nltk.corpus import stopwords

import csv

'''
Data
'''
target_nodes = ['ORGANIZATION', 'PERSON', 'LOCATION', 'GPE', 'FACILITY']

'''
Tokenize a text
'''
def _word_tokenize(text):
	_tokenized = nltk.word_tokenize(text)
	return _tokenized

'''
Normalizing to lower
'''
def _norm_to_lower(tokenized):
	looper = 0
	for token in tokenized:
			tokenized[looper] = token.lower()
			looper += 1
	return tokenized

#Probably seek company names at this phase
#before Lemmatization

'''
Removing stop words and small words
'''
def _remove_stop_words(tokenized):
	minlength = 2
	filtered = [token for token in tokenized if (not token in stopwords.words('english')) and len(token) >= minlength]
	return filtered

'''
Stemming
'''
def _stem(tokenized):
	porter = nltk.PorterStemmer()
	looper = 0
	for token in tokenized:
			tokenized[looper] = porter.stem(token)
			looper += 1
	return tokenized

'''
Lemmatization
'''
def _lemmatize(tokenized):
	lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
	looper = 0
	for token in tokenized:
		tokenized[looper] = lmtzr.lemmatize(token)
		looper += 1
	return tokenized

'''
Create FreqDist from tokenized text 
'''
def _freqencies(tokenized):
	mytext = nltk.Text(tokenized)
	fdist1 = FreqDist(mytext)
	return fdist1


'''
Extract Named Entities
https://gist.github.com/onyxfish/322906
'''
def extract_entity_names(t):
	entity_names = {}

	if hasattr(t, 'node') and t.node:
		if t.node in target_nodes:
			#this will be the named entity string:
			nes = ' '.join([child[0] for child in t])
			new = { 'ne': nes, 'type': t.node }
			entity_names.update(new)

			#entity_names.append(' '.join([child[0] for child in t]))
			#entity_keys.append(t.node)
		else:
			for child in t:
				entity_names.update(extract_entity_names(child))
	
	return entity_names

'''
Extract Named Entities v.2 Test
modified from http://timmcnamara.co.nz/post/2650550090/extracting-names-with-6-lines-of-python-code
'''
def extract_entities(text, nodetype=None):
	for sent in nltk.sent_tokenize(text):
		for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
			if hasattr(chunk, 'node'):
				if(nodetype):
					if chunk.node == nodetype:
						return chunk.node, ' '.join(c[0] for c in chunk.leaves())
				else:
					return chunk.node, ' '.join(c[0] for c in chunk.leaves())



				

