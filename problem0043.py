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
