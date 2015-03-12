# -*- coding: utf-8 -*-
# In England the currency is made up of pound, £, and pence, p, and there
# are eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

import time

t0 = time.clock()
answer = -1

memo = {}

def make_change(target,denoms):
    if target == 0:
        return 1
    elif target < 0:
        return 0
    elif len(denoms) == 0:
        return 0

    m = max(denoms)
    index = '{0},{1}'.format(target,m)
    if index in memo:
        return memo[index]

    memo[index] = make_change(target,denoms[:-1]) + make_change(target-m,denoms)

    return memo[index]

denoms = [1,2,5,10,20,50,100,200]
target = 200
answer = make_change(target,denoms)

print 'answer: {}'.format(answer) # 73682
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~3.6ms

