from util import *
from nltk.stem import PorterStemmer





class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""
		stemmer = PorterStemmer()
		reducedText = [[stemmer.stem(word) for word in sentence] for sentence in text]

		#Fill in code here
		
		return reducedText


