# The nth term of the sequence of triangle numbers is given by,
# t_n = n(n+1)/2; so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the
# word value is a triangle number then we shall call the word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text
# file containing nearly two-thousand common English words, how many are
# triangle words?

import time

def wordScore(w):
    return sum([ ord(c)-64 for c in w ])

def triangularNumsLessThan(n):
    return [i*(i+1)/2 for i in range(1,n)]

t0 = time.clock()

f = open('p042_words.txt','r')
words = f.read()
f.close()

words = words.split(',')
wordScores = [wordScore(w.strip('"')) for w in words]

triNums = triangularNumsLessThan(max(wordScores))
numTriWords = 0
for ws in wordScores:
    if ws in triNums:
        numTriWords += 1

print 'number of triangular words: {0}'.format(numTriWords)
print 'seconds elapsed: {0}'.format(time.clock()-t0)
