import time
import math
import numbertheory as nt
import itertools as it
import string

t0 = time.clock()
answer = 0

f = open('p059_cipher.txt')
message = f.read()
f.close()

cipher = map(int,message.split(','))
##counts = [cipher.count(k) for k in range(128)]

##print cipher
##for i,c in enumerate(counts):
##    if c > 0:
##        print i,c
##        answer += 1

passchars = map(ord,string.lowercase)
##print passchars

N = len(cipher)
commonWords = ['the','be','to','of','and','in','that','have','for']
bestScore = 0
bestKey = None
bestPlain = ''

for key in it.product(passchars,passchars,passchars):
    plain = [ key[i % 3] ^ cipher[i] for i in range(N) ]
    plain = ''.join(map(chr,plain))
    score = sum([1 if w in plain else 0 for w in commonWords])
##    if score > 5:
##        print plain
    if score > bestScore:
        bestScore = score
        bestKey = key
        bestPlain = plain
        answer = sum([ord(c) for c in plain])
        
print 'answer: {}'.format(bestPlain)
print 'seconds elapsed: {}'.format(time.clock()-t0)
