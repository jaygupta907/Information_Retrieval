from util import *

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, TreebankWordTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')



class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""
		stop_words = set(stopwords.words('english'))
		stopwordRemovedText = [[word for word in sentence if word.lower() not in stop_words] for sentence in text]

		#Fill in code here

		return stopwordRemovedText




	