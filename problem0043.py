# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
# 
# Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we
# note the following:
# 
# d_2d_3d_4=406 is divisible by 2
# d_3d_4d_5=063 is divisible by 3
# d_4d_5d_6=635 is divisible by 5
# d_5d_6d_7=357 is divisible by 7
# d_6d_7d_8=572 is divisible by 11
# d_7d_8d_9=728 is divisible by 13
# d_8d_9d_10=289 is divisible by 17
# 
# Find the sum of all 0 to 9 pandigital numbers with this property.

import time
import itertools as it

t0 = time.clock()
tot = 0

perms = it.permutations('0123456789')
for x in perms:
    d = [-1]+[int(c) for c in x] # the -1 is for alignment with the problem statement
    if d[4] % 2 != 0: continue
    if (d[3]+d[4]+d[5]) % 3 != 0: continue
    if d[6] != 5: continue
    if (10*d[5]+d[6]-2*d[7]) % 7 != 0: continue
    if (d[6]-d[7]+d[8]) % 11 != 0: continue
    if (10*d[7]+d[8]-9*d[9]) % 13 != 0: continue
    if (10*d[8]+d[9]-5*d[10]) % 17 != 0: continue
    n = int(''.join(x))
    print n
    tot += n

print 'sum of numbers with property: {0}'.format(tot)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
