# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *
from collections import Counter
import math

word1 ='مردان'
word2 = 'زنان'

file1 = open('data.txt','r')
file2 = open('data3.txt', 'r')
text1 = file1.read()
text2 = file2.read()

list = []
polarity = []
ph = []

normalizer = Normalizer()
normalizer.normalize(text1)

lemmatizer = Lemmatizer()
stemmer = Stemmer()

# ---------------------------------------// first file //-----------------------------------------
stemmer.stem(text1)
lemmatizer.lemmatize(text1)

sentences = sent_tokenize(text1)
tokens = word_tokenize(text1)
print(tokens)

count1 = tokens.count(word1)
count2 = tokens.count(word2)

tagger = POSTagger(model='resources/postagger.model')
'''
for sent,i in zip(sentences,range(1,1000)):
    tagged = tagger.tag(word_tokenize(sent))
    #print(tagged)
    for word in tagged:
        if word[1] == 'N':
            i = tagged.index(word)
            if tagged[i+1][1] == 'N':
                ph = word[0]+" "+ tagged[i+1][0]
                if ph not in list:
                    list.append(ph)

            i = tagged.index(word)
            if tagged[i + 1][1] == 'AJ':
                ph = word[0] + " " + tagged[i + 1][0]
                if ph not in list:
                    list.append(ph)

                    #print(ph)
            #print(tokens.count(word[0]))

''''''
for l in list:
    count = 0
    i1 = 0
    i2 = 0
    first = word_tokenize(l)[0]
    second = word_tokenize(l)[1]

    for sent in sentences:
        sent_tokens = word_tokenize(sent)
        if first in sent_tokens and sent_tokens[sent_tokens.index(first)+1] == second:
            if word1 in sent_tokens:
                i1 +=1

            if word2 in sent_tokens:
                i2 +=1
    if count2 != 0 and i1 != 0 and count1 != 0 and i2 != 0:
        polarity.append(math.log((count1 * i2) / (count2 * i1)))


if len(polarity) != 0:
    average = sum(polarity)/ float(len(polarity))
    print (average)
'''
j = 0
for i in range(0,100):
    j+=1
    print(sentences[20*i]+" "+sentences[20*i]+" "+sentences[20*i]+" "+sentences[20*i]+" "+sentences[20*i]+" "+sentences[20*i])
    t = tagger.tag(word_tokenize(sentences[20*i]+" "+sentences[20*i]+" "+sentences[20*i]+" "+sentences[20*i]+" "+sentences[20*i]+" "+sentences[20*i]))
    print(t)
    for tok in t:
        count = 0
        i1 = 0
        i2 = 0
        if tok[1] == 'N' and (t[t.index(tok)][1] == 'N' or t[t.index(tok)][1] == 'N'):
#        if t.index(tok) != len(t)-1:
            first = tok
            second = t[t.index(tok)+1]
#            #print('1111111111111')
#            str = tok+" "+(t[t.index(tok)+1])
#           #print(str)
            #print(ph)
#            if str in list:

            for sent in sentences:

                sent_tokens = word_tokenize(sent)
                if first in sent_tokens and sent_tokens[sent_tokens.index(first) + 1] == second:
                    if word1 in sent_tokens:
                        i1 += 1

                    if word2 in sent_tokens:
                        i2 += 1
            if count2 != 0 and i1 != 0 and count1 != 0 and i2 != 0:
                polarity.append(math.log((count1 * i2) / (count2 * i1)))
                print('p',j,polarity)


# -------------------------------------- // second file // ------------------------------------
'''
stemmer.stem(text2)
lemmatizer.lemmatize(text2)

sentences = sent_tokenize(text2)
tokens = word_tokenize(text2)

count1 = tokens.count(word1)
count2 = tokens.count(word2)

tagger = POSTagger(model='resources/postagger.model')

for sent,i in zip(sentences,range(1,1000)):
    tagged = tagger.tag(word_tokenize(sent))
    #print(tagged)
    for word in tagged:
        if word[1] == 'AJ':
            i = tagged.index(word)
            if tagged[i+1][1] == 'N':
                ph = word[0]+" "+ tagged[i+1][0]
                if ph not in list:
                    list.append(ph)
                    #print(ph)
            #print(tokens.count(word[0]))

for l in list:
    count = 0
    i1 = 0
    i2 = 0
    first = word_tokenize(l)[0]
    second = word_tokenize(l)[1]

    for sent in sentences:
        sent_tokens = word_tokenize(sent)
        if first in sent_tokens and sent_tokens[sent_tokens.index(first)+1] == second:
            if word1 in sent_tokens:
                i1 +=1

            if word2 in sent_tokens:
                i2 +=1
    if count2 != 0 and i1 != 0 and count1 != 0 and i2 != 0:
        polarity.append(math.log((count1 * i2) / (count2 * i1)))

if len(polarity) != 0:
    average = sum(polarity)/ float(len(polarity))
    print (average)


for i in range(0,30):
    j+=1
    print(sentences[10*i])
    t = word_tokenize(sentences[10*i])
    for tok in t:
        count = 0
        i1 = 0
        i2 = 0
        if t.index(tok) != len(t)-1:
            first = tok
            second = t[t.index(tok)+1]
            if tok+" "+(t[t.index(tok)+1]) in list:
                for sent in sentences:
                    sent_tokens = word_tokenize(sent)
                    if first in sent_tokens and sent_tokens[sent_tokens.index(first) + 1] == second:
                        if word1 in sent_tokens:
                            i1 += 1

                        if word2 in sent_tokens:
                            i2 += 1
                if count2 != 0 and i1 != 0 and count1 != 0 and i2 != 0:
                    polarity.append(math.log((count1 * i2) / (count2 * i1)))
                    print('p',j,polarity)
'''