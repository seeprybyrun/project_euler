import time
import math
import numbertheory as nt
import itertools as it
import string

t0 = time.clock()
answer = 0
MAXPOLYGON = 8

figNums = {}
nbrs = {}

# ranges computed so that the list only generates
# numbers with 4 digits
figNums[3] = [ (n*(n+1))/2 for n in range(45,141) ]
figNums[4] = [ n**2 for n in range(32,100) ]
figNums[5] = [ n*(3*n-1)/2 for n in range(26,82) ]
figNums[6] = [ n*(2*n-1) for n in range(23,71) ]
figNums[7] = [ n*(5*n-3)/2 for n in range(21,64) ]
figNums[8] = [ n*(3*n-2) for n in range(19,59) ]

##for i in range(3,9):
##    print figNums[i][0],figNums[i][1]
##    print figNums[i][-2],figNums[i][-1]

#print figNums[3]
k = MAXPOLYGON-3+1

print 'building {}-partite graph'.format(k)
for i in range(3,MAXPOLYGON+1):
    nbrs[i] = {}
    for n in figNums[i]:
        nbrsOfN = {}
        for j in range(1,k):
            nbrsOfNj = [m for m in figNums[(i-3-j)%k+3] if str(m)[:2] == str(n)[2:]]
            if nbrsOfNj:
                nbrsOfN[(i-3-j)%k+3] = nbrsOfNj
        if nbrsOfN:
            nbrs[i][n] = nbrsOfN
            #print 'nbrs[{}][{}] = {}'.format(i,n,nbrsOfN)

print 'searching for cycle'
j1 = 3
tracker = [j1]
for n1 in nbrs[j1]:
    for j2 in nbrs[j1][n1]:
        if j2 in tracker: continue
        tracker += [j2]
        for n2 in nbrs[j1][n1][j2]:
            if n2 not in nbrs[j2]: continue
            for j3 in nbrs[j2][n2]:
                if j3 in tracker: continue
                tracker += [j3]
                for n3 in nbrs[j2][n2][j3]:
                    if n3 not in nbrs[j3]: continue
                    for j4 in nbrs[j3][n3]:
                        if j4 in tracker: continue
                        tracker += [j4]
                        for n4 in nbrs[j3][n3][j4]:
                            if n4 not in nbrs[j4]: continue
                            for j5 in nbrs[j4][n4]:
                                if j5 in tracker: continue
                                tracker += [j5]
                                for n5 in nbrs[j4][n4][j5]:
                                    if n5 not in nbrs[j5]: continue
                                    for j6 in nbrs[j5][n5]:
                                        if j6 in tracker: continue
                                        tracker += [j6]
                                        assert sorted(tracker) == [3,4,5,6,7,8]
                                        for n6 in nbrs[j5][n5][j6]:
                                            if str(n1)[:2] == str(n6)[2:]:
                                                print n1,n2,n3,n4,n5,n6
                                                print tracker
                                                answer = n1+n2+n3+n4+n5+n6
                                        tracker = tracker[:-1]
                                tracker = tracker[:-1]
                        tracker = tracker[:-1]
                tracker = tracker[:-1]
        tracker = tracker[:-1]
    
## 2512 1281 8128 2882 8256 5625
## 7    8    6    5    3    4
print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
