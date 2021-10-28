#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a wordcloud from a text file

Created on Tue Oct 26 21:24:04 2021
@author: ece

"""

import wordcloud
import numpy as np

# words that don't mean much in isolation
words_to_remove=['those','these','for','of','and','on','then','than','a',
				 'an','is','was','if','to','as','one','but','no','will',
				 'be','has','been','this','that','may','in','can','by',
				 'whether','or','from','with','many','my','other','at',
				 'are','their','I','when','they','all','so','not','some',
				 'which','its','myself','very','upon','our','do','the',
				 'it','whatsoever','','about','there','any','such','were',
                          	 'have','would','he','his','any','only','about','total',
                         	 'more','had','who','during','we']

# upload a text file of a book
book='/Users/ece/Documents/GitHub/python_ex/eclipse.txt'  # Book is titled 'The Story of Eclipses', taken from the Project Gutenberg
with open(book) as f:
	contents=f.read()

# split words and make them lowercase, remove spaces
words=contents.split()
for word in range(len(words)):
	words[word]=words[word].lower()
	words[word]=words[word].strip()

# remove irrelevant words to speed up code - first pass
new_words=words
for word in words_to_remove:
	new_words=list(filter(lambda a: a != word, new_words))
words=new_words

# remove punctuation & numbers
new_list=[]
for word in words:
	w2 = ''.join(filter(str.isalpha, word))
	new_list.append(w2)
words=new_list

# remove irrelevant words - second pass punctuation corrected
new_words=words
for word in words_to_remove:
	new_words=list(filter(lambda a: a != word, new_words))
words=new_words

# remove words that are shorter than 2 letters
for word in words:
	if len(word)<2:
		words.remove(word)

# get a list of unique words
unique_words=list(set(words))

# count each word put in dictionary
new_dict={}
for w in unique_words:
	new_dict[w]=words.count(w)

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(new_dict)
myimage=cloud.to_array()
plt.imshow(myimage,interpolation = 'nearest')
plt.axis('off')
plt.show()

