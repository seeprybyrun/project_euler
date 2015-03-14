# In the game, Monopoly, the standard board is set up in the following way:
# 
# GO  A1 CC1 A2 T1 R1 B1 CH1 B2  B3 JAIL
# H2                                C1
# T2                                U1
# H1                                C2
# CH3                               C3
# R4                                R2
# G3                                D1
# CC3                               CC2
# G2                                D2
# G1                                D3
# G2J F3 U2  F2 F1 R3 E3 E2  CH2 E1 FP
# 
# A player starts on the GO square and adds the scores on two 6-sided dice to
# determine the number of squares they advance in a clockwise direction.
# Without any further rules we would expect to visit each square with equal
# probability: 2.5%. However, landing on G2J (Go To Jail), CC (community
# chest), and CH (chance) changes this distribution.
# 
# In addition to G2J, and one card from each of CC and CH, that orders the
# player to go directly to jail, if a player rolls three consecutive doubles,
# they do not advance the result of their 3rd roll. Instead they proceed
# directly to jail.
# 
# At the beginning of the game, the CC and CH cards are shuffled. When a
# player lands on CC or CH they take a card from the top of the respective
# pile and, after following the instructions, it is returned to the bottom of
# the pile. There are sixteen cards in each pile, but for the purpose of this
# problem we are only concerned with cards that order a movement; any
# instruction not concerned with movement will be ignored and the player will
# remain on the CC/CH square.
# 
# Community Chest (2/16 cards):
# 1. Advance to GO
# 2. Go to JAIL
# 
# Chance (10/16 cards):
# 1. Advance to GO
# 2. Go to JAIL
# 3. Go to C1
# 4. Go to E3
# 5. Go to H2
# 6. Go to R1
# 7. Go to next R (railway company)
# 8. Go to next R
# 9. Go to next U (utility company)
# 10. Go back 3 squares.
# 
# The heart of this problem concerns the likelihood of visiting a particular
# square. That is, the probability of finishing at that square after a roll.
# For this reason it should be clear that, with the exception of G2J for which
# the probability of finishing on it is zero, the CH squares will have the
# lowest probabilities, as 5/8 request a movement to another square, and it is
# the final square that the player finishes at on each roll that we are
# interested in. We shall make no distinction between "Just Visiting" and
# being sent to JAIL, and we shall also ignore the rule about requiring a
# double to "get out of jail", assuming that they pay to get out on their next
# turn.
# 
# By starting at GO and numbering the squares sequentially from 00 to 39 we
# can concatenate these two-digit numbers to produce strings that correspond
# with sets of squares.
# 
# Statistically it can be shown that the three most popular squares, in order,
# are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square
# 00. So these three most popular squares can be listed with the six-digit
# modal string: 102400.
# 
# If, instead of using two 6-sided dice, two 4-sided dice are used, find the
# six-digit modal string.

import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy
import re
import random

from math import floor,sqrt,log

inf = float('inf')

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def printByRow(matrix):
    for row in matrix:
        print row

def dotProd(v,w):
    assert len(v) == len(w)
    n = len(v)
    return sum([v[i]*w[i] for i in range(n)])

def matVecProd(A,v):
    m = len(A)
    n = len(A[0])
    assert len(v) == n
    return [ dotProd(A[i],v) for i in range(m) ]

assert dotProd([0,1],[1,0]) == 0
assert matVecProd([[0,1],[1,0]],[1,-1]) == [-1,1]

factorial = [1,1,2,6,24,120,720,5040,40320,362880]

# This version implements a Markov model found in the solution forums

t0 = time.clock()
answer = ''
numIterations = 10**2
dice = [4,4]
numSpaces = 40
spaces = [str(i) if i > 9 else '0'+str(i) for i in range(numSpaces)]
states = [state for state in it.product(spaces,[0,1,2])] # [0,1,2] is numDoubles
possibleRolls = [roll for roll in it.product(*map(lambda x:range(1,x+1),dice))]

assert states[0] == ('00',0)

# build the transition probability matrix
transitionProbs = {}
for s in states:
    transitionProbs[s] = {t: 0. for t in states}
    for roll in possibleRolls:
        onCommChest = False
        onChance = False
        thisProb = 1./len(possibleRolls)
        space = (int(s[0]) + roll[0] + roll[1]) % numSpaces
        doubles = (s[1] + 1) if roll[0] == roll[1] else 0

        if doubles == 3 or space == 30: # go to jail
            space = 10
            doubles = 0
        elif space in [2,17,33]: # community chest
            onCommChest = True
        elif space in [7,22,36]: # chance
            onChance = True

        if onCommChest:
            t = (str(space) if space > 9 else '0'+str(space),doubles)
            transitionProbs[s][t] += thisProb * 14./16.
            t_go = ('00',doubles)
            transitionProbs[s][t_go] += thisProb * 1./16.
            t_jail = ('10',0)
            transitionProbs[s][t_jail] += thisProb * 1./16.
        elif onChance:
            t = (str(space) if space > 9 else '0'+str(space),doubles)
            transitionProbs[s][t] += thisProb * 6./16.
            
            t_go = ('00',doubles)
            transitionProbs[s][t_go] += thisProb * 1./16.
            t_jail = ('10',0)
            transitionProbs[s][t_jail] += thisProb * 1./16.
            
            t_c1 = ('11',doubles)
            transitionProbs[s][t_c1] += thisProb * 1./16.
            t_e3 = ('24',doubles)
            transitionProbs[s][t_e3] += thisProb * 1./16.
            t_h2 = ('39',doubles)
            transitionProbs[s][t_h2] += thisProb * 1./16.
            t_r1 = ('05',doubles)
            transitionProbs[s][t_r1] += thisProb * 1./16.
            
            if space == 7:
                t_nextR = ('15',doubles)
                transitionProbs[s][t_nextR] += thisProb * 2./16.
                t_nextU = ('12',doubles)
                transitionProbs[s][t_nextU] += thisProb * 1./16.
                t_back3 = ('04',doubles)
                transitionProbs[s][t_back3] += thisProb * 1./16.
            elif space == 22:
                t_nextR = ('25',doubles)
                transitionProbs[s][t_nextR] += thisProb * 2./16.
                t_nextU = ('28',doubles)
                transitionProbs[s][t_nextU] += thisProb * 1./16.
                t_back3 = ('19',doubles)
                transitionProbs[s][t_back3] += thisProb * 1./16.
            else: # space is 36
                t_nextR = ('05',doubles)
                transitionProbs[s][t_nextR] += thisProb * 2./16.
                t_nextU = ('12',doubles)
                transitionProbs[s][t_nextU] += thisProb * 1./16.
                # if moving back, have to account for commChest
                t_back3a = ('33',doubles) # noop
                transitionProbs[s][t_back3a] += thisProb * 1./16. * 14./16.
                t_back3b = ('00',doubles) # gd2g
                transitionProbs[s][t_back3b] += thisProb * 1./16. * 1./16.
                t_back3c = ('10',0)       # gd2j
                transitionProbs[s][t_back3c] += thisProb * 1./16. * 1./16.
        else:
            t = (str(space) if space > 9 else '0'+str(space),doubles)
            transitionProbs[s][t] += thisProb

    assert abs(sum([transitionProbs[s][t] for t in states]) - 1.) < 10**-6

matrix = [ [transitionProbs[s][t] for s in states] for t in states ]
vector = [0.] * len(matrix)
vector[0] = 1.

for i in range(numIterations):
    vector = matVecProd(matrix,vector)
    assert abs(sum(vector) - 1.) < 10**-6

spaceProbs = [ vector[3*i] + vector[3*i+1] + vector[3*i+2] for i in range(numSpaces) ]
topSpaces = sorted(spaces,key=lambda x: spaceProbs[int(x)],reverse=True)
##for s in topSpaces:
##    print s, spaceProbs[int(s)]

answer += '0' if topSpaces[0] < 10 else ''
answer += str(topSpaces[0])
answer += '0' if topSpaces[1] < 10 else ''
answer += str(topSpaces[1])
answer += '0' if topSpaces[2] < 10 else ''
answer += str(topSpaces[2])
        
print 'answer: {}'.format(answer) # 101524
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~0.258s
