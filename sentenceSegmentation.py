from util import *

from nltk.tokenize import sent_tokenize
import re


class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
		
		# Split the text using the delimiters '.', '!', '?'
		split_text = re.split(r'[.!?]\s', text)
	
		# Remove empty strings and strip spaces from the sentences
		segmentedText = [s.strip() for s in split_text if s.strip()]
		
		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = sent_tokenize(text)
		return segmentedText