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
