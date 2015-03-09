import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy

from math import floor,sqrt,log

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

factorial = [1,1,2,6,24,120,720,5040,40320,362880]

def digitFactorial(n):
    return sum([factorial[int(c)] for c in str(n)])

t0 = time.clock()
answer = 0
MAX = 6
TARGET = 60

for e in range(1,MAX+1):
    for x in it.combinations_with_replacement('9876543210',e):
        i = int(''.join(x))
        prev3 = i
        prev2 = i
        prev1 = i
        df = digitFactorial(i)
        numNonRepeatingTerms = 1
        while True:
            if df == prev3 or df == prev2 or df == prev1:
                break
            numNonRepeatingTerms += 1
            prev3,prev2,prev1,df = prev2,prev1,df,digitFactorial(df)
        if numNonRepeatingTerms == TARGET:
            numPerms = factorial[e]
            for c in set(x):
                numPerms /= factorial[x.count(c)]
            numBadPerms = 0
            if '0' in x:
                numBadPerms = factorial[e-1]
                for c in set(x):
                    if c == '0':
                        numBadPerms /= factorial[x.count(c)-1]
                    else:
                        numBadPerms /= factorial[x.count(c)]
            answer += (numPerms - numBadPerms)
            print i

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
