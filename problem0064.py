import time
import math
import numbertheory as nt
import itertools as it
from decimal import *
import re

from math import sqrt
from math import floor
from math import log

##def continuedFractionExpansion(x,numConvergents):
##    ret = '['
##    for i in range(numConvergents):
##        intPart = int(floor(x))
##        ret += str(intPart)
##        if i == 0:
##            ret += ';'
##        else:
##            ret += ','
##        x -= intPart
##        if x == 0: break
##        x = 1/x
##    ret += ']'
##    return ret

##def continuedFractionExpansionSqrt(n,numConvergents):
##    ret = ''
####    ret += '['
##    x = int(floor(sqrt(n)))
##    prevDenom = 1
##    a = x
##    for i in range(numConvergents):
##        ret += str(x) + (';' if i == 0 else ',')
##        if n == a**2:
##            break
##        else:
##            denom = (n - a**2)/prevDenom
##            numer = sqrt(n) + a
##            x = 0
##            while numer/denom > 1:
##                x += 1
##                a -= denom
##                numer = sqrt(n) + a
##            prevDenom = denom
##            a *= -1
####    ret += ']'
##    return ret

def continuedFractionExpansionSqrt(n,numConvergents):
    ret = []
    x = int(floor(sqrt(n)))
    prevDenom = 1
    a = x
    for i in range(numConvergents):
        ret += [x]
        if n == a**2:
            break
        else:
            denom = (n - a**2)/prevDenom
            numer = sqrt(n) + a
            x = 0
            while numer/denom > 1:
                x += 1
                a -= denom
                numer = sqrt(n) + a
            prevDenom = denom
            a *= -1
    return ret

def periodOfContinuedFractionExpansionSqrt(n):
    x = int(floor(sqrt(n)))
    if x*x == n: return 0
    prevPairs = []
    prevDenom = 1
    a = x
    pd = 0
    while True:
        denom = (n - a**2)/prevDenom
        numer = sqrt(n) + a
        x = 0
        while numer/denom > 1:
            x += 1
            a -= denom
            numer = sqrt(n) + a
        if (a,denom) in prevPairs:
            return pd
        else:
            prevPairs.append((a,denom))
            prevDenom = denom
            a *= -1
            pd += 1

##print periodOfContinuedFractionExpansionSqrt(2)
##print periodOfContinuedFractionExpansionSqrt(3)
##print periodOfContinuedFractionExpansionSqrt(5)
##print periodOfContinuedFractionExpansionSqrt(6)
##print periodOfContinuedFractionExpansionSqrt(7)
##print periodOfContinuedFractionExpansionSqrt(8)
##print periodOfContinuedFractionExpansionSqrt(10)
##print periodOfContinuedFractionExpansionSqrt(11)
##print periodOfContinuedFractionExpansionSqrt(12)
##print periodOfContinuedFractionExpansionSqrt(13)
##print periodOfContinuedFractionExpansionSqrt(23)

def findShortestPeriodicSubstring(s):
    """Returns the shortest substring of s that occurs periodically
until the end of s. The output need not start s. For example, if
s == 'abcbcbcb', then this function returns 'cb'. However, if s ==
'abcbcbcbc', then this function returns 'bc'. Returns [] if no
substring is found that repeats until the end of the string."""
    for L in range(1,len(s)/2+1): # L is length
        maxLInS = len(s)/L
        for sp in range(len(s)-maxLInS*L,len(s)-2*L+1,L): # sp is start position
            try:
                assert (len(s) - sp) % L == 0
            except:
                print len(s), sp, L
                assert False
            testString = s[sp:sp+L]
            if s[sp:] == testString * ((len(s)-sp)/L):
                return testString
    return []

def findLongestPeriodicSubstring(s):
    """Returns the longest substring of s that occurs periodically
until the end of s. The output need not start s. For example, if
s == 'abcbcbcb', then this function returns 'cb'. However, if s ==
'abcbcbcbc', then this function returns 'bcbc'. Returns [] if no
substring is found that repeats until the end of the string."""
    ret = []
    for L in range(len(s)/2+1,0,-1): # L is length
        maxLInS = len(s)/L
        for sp in range(len(s)-maxLInS*L,len(s)-2*L+1,L): # sp is start position
            try:
                assert (len(s) - sp) % L == 0
            except:
                print len(s), sp, L
                assert False
            testString = s[sp:sp+L]
            if s[sp:] == testString * ((len(s)-sp)/L):
                return testString
    return ret

def removeRedundancies(s):
    for i in range(1,len(s)):
        if len(s) % i != 0: continue
        t = s[:i]
        if s == t * (len(s)/i): return t
    return s

##print removeRedundancies('abcabc')
##print removeRedundancies('aaaaaa')
##print removeRedundancies('abcdef')

##print findPeriodicSubstring('abcbcbcb')
##print findPeriodicSubstring('abcbcbcbc')
##print findPeriodicSubstring('abc')
##print findPeriodicSubstring('aaa')
##print findPeriodicSubstring('a')
##print findPeriodicSubstring('')
##print findPeriodicSubstring('1;2,2,2,2,2,2,')
##print findPeriodicSubstring('1;1,2,1,2,1,2,')
##print findPeriodicSubstring(continuedFractionExpansionSqrt(2,10))
##print findPeriodicSubstring(continuedFractionExpansionSqrt(3,10))
##print findPeriodicSubstring(continuedFractionExpansionSqrt(23,10))
##print findPeriodicSubstring(continuedFractionExpansionSqrt(23,4))

##for i in range(1,26):
##    print continuedFractionExpansionSqrt(i,20)

t0 = time.clock()

##MAX = 100
##sqrtMAX = int(floor(sqrt(MAX)))
##period = [-1] * (MAX+1)
##unfilled = set(range(1,MAX+1)) - set([i**2 for i in range(1,sqrtMAX+1)])
##k = 8
##while unfilled and k <= 2**10:
##    toRemove = set()
##    for d in unfilled:
##        ps = findPeriodicSubstring(continuedFractionExpansionSqrt(d,k))
##        if ps:
##            pd = ps.count(',')
##            print 'd={},pd={}:{}'.format(d,pd,ps)
##            period[d] = pd
##            toRemove.add(d)
##    unfilled -= toRemove
##    print '{} remaining in unfilled, k = {}'.format(len(unfilled),k)
##    k *= 2

# original solution: ~29 seconds
##MAX = 10000
##sqrtMAX = int(floor(sqrt(MAX)))
##squares = [i**2 for i in range(1,sqrtMAX+1)]
##period = [0] * (MAX+1)
##
##for d in range(1,MAX+1):
##    if d % (MAX/20) == 0: print d
##    if d in squares: continue
####        print 'skipping d={}'.format(d)
####        continue
##    if d-1 in squares:
##        period[d] = 1
##        continue
##    # max length of period is ~0.3*sqrt(d)*log(d) (Cohn, THE LENGTH OF THE
##    # PERIOD OF THE SIMPLE CONTINUED FRACTION OF d^{1/2}, Pacific Journal
##    # of Mathematics, Vol. 71, No. 1, 1977)
##    k = int(floor( 0.7 * sqrt(d)*log(d) ))
##    expansion = continuedFractionExpansionSqrt(d,k)
##    ps = removeRedundancies(findLongestPeriodicSubstring(expansion))
##    pd = len(ps) #ps.count(',')
##    period[d] = pd
####    print d,pd,ps
####            # check that it's not a false positive by confirming the
####            # next few periods are the same
####            if pd == 1:
####                continue
####            numPdsToChk = 10
####            checkStr = continuedFractionExpansionSqrt(d,k+numPdsToChk*pd)[-numPdsToChk*len(ps):]
####            if checkStr == numPdsToChk*ps:
####                period[d] = pd
####                #print '{},{}'.format(d,k)
####                break
####            else:
####                print 'false positive for d={},k={}'.format(d,k)
##
##answer = sum(map(lambda x: x % 2,period))

# new solution based on forum posts:
answer = 0
MAX = 10000
for d in range(1,MAX+1):
    if periodOfContinuedFractionExpansionSqrt(d) % 2 == 1:
        answer += 1

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
