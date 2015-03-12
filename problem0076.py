# It is possible to write five as a sum in exactly six different ways:
# 
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# 
# How many different ways can one hundred be written as a sum of at least
# two positive integers?

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

# Assume partition is given as a list [k_1,k_2,...,k_n], where
# k_i represents the number of dots in the ith column of the Ferrers
# diagram corresponding to the partition (in English notation). The
# next partition is then given by deducting 1 from the rightmost k_i of
# maximum value and adding 1 to the leftmost k_i of whose value is at least
# two less than the maximum value.
# If partition is a partition of n, then starting from [n,0,...,0],
# iterating this procedure yields all partitions of n, ending at
# [1,1,...,1].
def nextPartition(partition):
    assert sum(partition) == len(partition)
    assert sorted(partition,reverse=True) == partition
    
    # no next partition can be made if the maximum term is 1
    maxTerm = partition[0]
    if maxTerm == 1:
        return None

    # First, find the rightmost index of the maximum element in the
    # partition. (Note: partitions in the form given above are sorted.)
    n = len(partition)
    maxTermIndex = n - 1 - partition[::-1].index(maxTerm)

    # Now find the first element that is at least 2 less than the max value
    termToIncrease = -1
    for i in range(maxTermIndex+1,n):
        if maxTerm - partition[i] >= 2:
            termToIncrease = i
            break
    assert termToIncrease >= 0

    ret = copy(partition)
    ret[maxTermIndex] -= 1
    ret[termToIncrease] += 1

    assert sum(ret) == len(ret)
    assert sorted(ret,reverse=True) == ret

    return ret

assert nextPartition([2,0]) == [1,1]
assert not nextPartition([1,1])
assert nextPartition([4,0,0,0]) == [3,1,0,0]
assert nextPartition([3,1,0,0]) == [2,2,0,0]
assert nextPartition([2,2,0,0]) == [2,1,1,0]
assert nextPartition([2,1,1,0]) == [1,1,1,1]
assert not nextPartition([1,1,1,1])

t0 = time.clock()
answer = 0
n = 10

partition = [n] + [0] * (n-1)
answer = 1
while partition:
    print partition
    partition = nextPartition(partition)
    answer += 1

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
