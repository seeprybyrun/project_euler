import time
import math
import numbertheory as nt
import itertools as it

from math import log10
from math import floor
from math import ceil

t0 = time.clock()
answer = float('inf')
CLIQUELENGTH = 5
numDigits = 1

# very fast solution that throws cubes into bins according to their digital
# representation, sorted; then checks to see if any bins have exactly 5 elements
# (check and reset the bins when the number of digits in the cubes increases)
while True:
    lowerBound = int(ceil(10**((numDigits-1)/3.0)))
    upperBound = int(ceil(10**(numDigits/3.0)))
    cubes = [n**3 for n in range(lowerBound,upperBound)]
    cliques = {}
    for c in cubes:
        s = ''.join(sorted(str(c)))
        if s in cliques:
            cliques[s] += [c]
        else:
            cliques[s] = [c]
    if CLIQUELENGTH in [len(cliques[s]) for s in cliques]:
        for s in cliques:
            if len(cliques[s]) == CLIQUELENGTH:
                answer = min(min(cliques[s]),answer)
        break
    if answer < float('inf'):
        break
    numDigits += 1

# my original solution below: way too much structure, since I didn't realize that
# the connected components of the graph were themselves cliques :-o
# lots of optimizations needed to make it run within 60 seconds: e.g.,
# only checking cubes that have the same number of digits as a given cube

##MAXCUBE = 8500
##print 'building the graph'
##cubes = [n**3 for n in range(MAXCUBE+1)]
##nbrs = {c:set([]) for c in cubes}
##for i,c in enumerate(cubes):
##    if c == 0: continue
##    numDigits = floor(log10(c))+1
##    upperBound = min(int(ceil(10**(numDigits/3.0))),MAXCUBE+1)
##    for j in range(i+1,upperBound):
####        if c >= d: continue
####        if floor(log10(c)) < floor(log10(d)): break
##        d = cubes[j]
##        if sorted(str(c)) == sorted(str(d)):
##            nbrs[c] |= set([d])
##
##print 'looking for clique'
##for c1 in cubes:
##    for c2 in nbrs[c1]:
##        for c3 in nbrs[c1] & nbrs[c2]:
##            for c4 in nbrs[c1] & nbrs[c2] & nbrs[c3]:
##                for c5 in nbrs[c1] & nbrs[c2] & nbrs[c3] & nbrs[c4]:
##                    print c1,c2,c3,c4,c5
##                    answer = min(c1,answer) # since ordered so that c1 < cj                    

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
