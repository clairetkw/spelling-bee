import json
import pandas as pd
from random import choice
import re

with open('data/words_dictionary.json') as inputFile:
    inputJson = json.load(inputFile)

# filter dictionary to only include words 4-9 characters long
outputPy = [x for x in inputJson if len(x) > 3 and len(x) < 10]

words = pd.read_csv('data/unigram_freq.csv')
swearWords = list(pd.read_csv('data/swear_words.csv'))

# get list of most commonly used words as strings
commonWords = list(words.loc[(words['count']>=2000000)].astype(str).word.values)

# get list of words that can be pangrams 
pangrams = [i for i in commonWords if len(i) < 10 and len(set(i)) == 7]
# total pangrams: 2452

def refresh():
    reset = False

    while reset == False:
        global targetWord
        global targetSet
        # pick a random word from pangrams
        targetWord = choice(pangrams)
                
        # find all unique letters that form targetWord
        targetSet = ''.join(set(targetWord))
        # print(targetSet)

        global randomLetter
        # pick a random letter from that word
        randomLetter = choice(targetWord)
        # print(randomLetter)

        global n
        # set up filters for unique letters + random letter
        m = re.compile('^[%s]+$'%(targetSet))
        n = re.compile('[%s]'%(randomLetter))

        # find words in the filtered dictionary that match conditions m and n, are common words, and are not swear words
        preAnswerSet = [w for w in outputPy if m.match(w) is not None and n.search(w) is not None and w in commonWords and w not in swearWords]

        global answerSet
        global answerSetCopy
        # arrange preAnswerSet by decreasing frequency of use 
        answerSet = [x for x in commonWords if x in preAnswerSet]
        del answerSet[30:]
        answerSetCopy = answerSet
        reset = True

refresh()