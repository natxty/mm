import sys, re, time, string, json, functions, nltk
from nltk.probability import *
from nltk.corpus import stopwords


def extract_job_titles(text):

	'''
	Set up vars
	'''
	titles = {}
	reports = {}
	timings = []

	'''
	regex
	'''
	rdict = {
		'n/a': 'None',
		'3d/2d': '2d-3d',
		'2d/3d': '2d-3d',
		'hci/ux/ui': 'ui-ux',
		'ui/ux': 'ui-ux',
		'ux/ui': 'ui-ux',
		'sr ': 'senior ',
	}
	robj = re.compile('|'.join(rdict.keys()))

	#more specific regex dict:
	xdict = {
		'dir': 'director',
		'pr': 'public relations',
		'cd': 'creative director',
		'bad': 'art director',
		'md': 'marketing director',
		'acd': 'associate creative director',
		'dp': 'director of photography',
		'evp': 'executive vice president',
		'svp': 'senior vice president',
		'vp': 'vice president',
	}

	xobj = re.compile('$|'.join(xdict.keys()))

	#for detecting "and"
	andpattern = re.compile(r'\band\b')


	'''
	analyze input
	'''
	#if we got text:
	if text:
		'''
		1. Initial cleanup
		'''
		#get rid of some whitespace:
		text = text.lower().strip()

		#strip some punctuation:
		text = re.sub(r"\!|\?|\.", "", text)

		#experimental :: convert "and" to &, since we split() on that later
		text = re.sub(r"\band\b", "&", text)

		#now, re.sub() from the first dict of replacement values
		text = robj.sub(lambda m: rdict[m.group(0)], text)

		#tackle some special occurrences that don't regex well:
		text = text.replace("a&r", 'a-r')
		text = text.replace("sr.", "senior")
		text = text.replace("(other)", "None")
		text = text.replace("designer (ux/web)", "ux designer/web designer")

		'''
		2. Break up groups into individual titles, as best we can
		   split on the most common dividers:
		'''
		l = re.compile("/|,|&|\|").split(text)

		#iterate through the parts for some more specific replacements:
		for x in l:
			x = x.strip()
			x = xobj.sub(lambda m: xdict[m.group(0)], x)

			#add single "title" values to the output dict
			if x in reports:
				reports[x] += 1
			else:
				reports[x] = 1

		return json.dumps(reports)

	else:
		return json.dumps('No text given')


if __name__ == '__main__':
	titles = extract_job_titles(sys.argv[1])
	print titles

