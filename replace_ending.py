#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 00:47:18 2021

@author: ece
"""

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
    # sentence='The weather is nice in May'
    # old='May'
    # new='April'
	if old in sentence:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		words=sentence.split()
		word=words[-1]

		if word==old and sentence.count(old)==1:
			i = sentence.index(old)
			new_sentence = sentence[:i] + new
			return new_sentence
		elif word==old and sentence.count(old)!=1:
			i = sentence.index(old)
			k=i+len(old)
			chunk= sentence[(k+1):]
			l=chunk.index(old)
			new_sentence=sentence[:k] + ' ' + chunk[:l] + new
			return new_sentence
	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
