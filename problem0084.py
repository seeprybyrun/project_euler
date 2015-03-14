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

factorial = [1,1,2,6,24,120,720,5040,40320,362880]

t0 = time.clock()
answer = ''
numRolls = 10**6
dice = [4,4]
numSpaces = 40
numTimesLanded = [0] * numSpaces
currSquare = 0
numDoubles = 0

communityChestCards = ['noop']*14 + ['go','jail']
chanceCards = ['noop']*6 + ['go','jail','c1','e3','h2','r1','nextR','nextR','nextU','back3']

# todo: shuffle community chest and chance cards
# shortcut: not implementing shuffle; instead just randomly drawing from the
# two decks

##communityChestTopCard = 0
##chanceTopCard = 0

for i in range(numRolls):
    # roll dice
    rolls = [random.randint(1,die) for die in dice]

    # doubles check
    if len(set(rolls)) == 1:
        numDoubles += 1
    else:
        numDoubles = 0

    # move the avatar
    currSquare += sum(rolls)
    currSquare %= numSpaces

    action = 'noop'

    # check for third double in a row
    if numDoubles == 3:
        action = 'jail'
    elif currSquare == 30: # GO TO JAIL!
        action = 'jail'
    elif currSquare in [2,17,33]: # community chest
        communityChestTopCard = random.randint(0,len(communityChestCards)-1)
        action = communityChestCards[communityChestTopCard]
##        communityChestTopCard += 1
##        communityChestTopCard %= len(communityChestCards)
    elif currSquare in [7,22,36]: # chance
        chanceTopCard = random.randint(0,len(chanceCards)-1)
        action = chanceCards[chanceTopCard]
##        chanceTopCard += 1
##        chanceTopCard %= len(chanceCards)

    if (action == 'jail') or (action == 'back3' and currSquare == 33):
        # GO TO JAIL!
        currSquare = 10
        numDoubles = 0
    elif action == 'go':
        currSquare = 0
    elif action == 'c1':
        currSquare = 11
    elif action == 'e3':
        currSquare = 24
    elif action == 'h2':
        currSquare = 39
    elif action == 'r1':
        currSquare = 5
    elif action == 'nextR':
        if currSquare < 5 or currSquare > 35:
            currSquare = 5
        elif 5 < currSquare < 15:
            currSquare = 15
        elif 15 < currSquare < 25:
            currSquare = 25
        elif 25 < currSquare < 35:
            currSquare = 35
        else:
            assert False
    elif action == 'nextU':
        if currSquare < 12 or currSquare > 28:
            currSquare = 12
        elif 12 < currSquare < 28:
            currSquare = 28
        else:
            assert False
    elif action == 'back3':
        currSquare -= 3
        # should we draw another card if this causes us to land on another
        # chance/community chest?

    # update square-landings
    numTimesLanded[currSquare] += 1

topSquares = sorted(range(numSpaces),key=lambda x: numTimesLanded[x],reverse=True)
for i in topSquares[:5]:
    print i, 100.*numTimesLanded[i]/numRolls

answer += '0' if topSquares[0] < 10 else ''
answer += str(topSquares[0])
answer += '0' if topSquares[1] < 10 else ''
answer += str(topSquares[1])
answer += '0' if topSquares[2] < 10 else ''
answer += str(topSquares[2])
        
print 'answer: {}'.format(answer) # 101524
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~7.39s
