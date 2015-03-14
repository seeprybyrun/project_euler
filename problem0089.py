# For a number written in Roman numerals to be considered valid there are
# basic rules which must be followed. Even though the rules allow some numbers
# to be expressed in more than one way there is always a "best" way of writing
# a particular number.
# 
# For example, it would appear that there are at least six ways of writing the number sixteen:
# 
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
# 
# However, according to the rules only XIIIIII and XVI are valid, and the last
# example is considered to be the most efficient, as it uses the least number
# of numerals.
# 
# The 11K text file, roman.txt (right click and 'Save Link/Target As...'),
# contains one thousand numbers written in valid, but not necessarily minimal,
# Roman numerals; see About... Roman Numerals for the definitive rules for
# this problem.
# 
# Find the number of characters saved by writing each of these in their
# minimal form.
#
# Note: You can assume that all the Roman numerals in the file contain no more
# than four consecutive identical units.
#
# DA RULES:
#
# Traditional Roman numerals are made up of the following denominations:
# 
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# 
# 1. Numerals must be arranged in descending order of size.
# 2. M, C, and X cannot be equalled or exceeded by smaller denominations.
# 3. D, L, and V can each only appear once.
# 
# In addition to the three rules given above, if subtractive combinations are used then the following four rules must be followed.
# 
# 4. Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
# 5. I can only be placed before V and X.
# 6. X can only be placed before L and C.
# 7. C can only be placed before D and M.

import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy
import re
import random

from math import floor,sqrt,log,ceil

inf = float('inf')
factorial = [1,1,2,6,24,120,720,5040,40320,362880]

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def printByRow(matrix):
    for row in matrix:
        print row

def romanToDecimal(r):
    n = len(r)
    values = []
    for c in r:
        if c == 'M':
            values.append(1000)
        if c == 'D':
            values.append(500)
        if c == 'C':
            values.append(100)
        if c == 'L':
            values.append(50)
        if c == 'X':
            values.append(10)
        if c == 'V':
            values.append(5)
        if c == 'I':
            values.append(1)
    for i in range(n-1):
        if values[i] < values[i+1]:
            values[i+1] -= values[i]
            values[i] = 0
    return sum(values)

assert romanToDecimal('XIIIIII') == 16
assert romanToDecimal('XVI') == 16
assert romanToDecimal('XIV') == 14
assert romanToDecimal('XIIII') == 14
assert romanToDecimal('MCI') == 1101
assert romanToDecimal('CDXLIV') == 444
assert romanToDecimal('MDCLXVI') == 1666
assert romanToDecimal('CMC') == 1000
assert romanToDecimal('CMXCIX') == 999

def decimalToMinimalRoman(d):
    r = ''
    while d >= 1000:
        d -= 1000
        r += 'M'
    if d >= 900:
        d -= 900
        r += 'CM'
    if d >= 500:
        d -= 500
        r += 'D'
    if d >= 400:
        d -= 400
        r += 'CD'
    while d >= 100:
        d -= 100
        r += 'C'
    if d >= 90:
        d -= 90
        r += 'XC'
    if d >= 50:
        d -= 50
        r += 'L'
    if d >= 40:
        d -= 40
        r += 'XL'
    while d >= 10:
        d -= 10
        r += 'X'
    if d >= 9:
        d -= 9
        r += 'IX'
    if d >= 5:
        d -= 5
        r += 'V'
    if d >= 4:
        d -= 4
        r += 'IV'
    while d >= 1:
        d -= 1
        r += 'I'
    return r

assert decimalToMinimalRoman(16) == 'XVI'
assert decimalToMinimalRoman(14) == 'XIV'
assert decimalToMinimalRoman(1101) == 'MCI'
assert decimalToMinimalRoman(444) == 'CDXLIV'
assert decimalToMinimalRoman(1666) == 'MDCLXVI'
assert decimalToMinimalRoman(1000) == 'M'
assert decimalToMinimalRoman(999) == 'CMXCIX'

# start script here
t0 = time.clock()
answer = 0

f = open('data/p089_roman.txt','r')
for line in f.readlines():
    r1 = line.strip()
    d = romanToDecimal(r1)
    r2 = decimalToMinimalRoman(d)
    answer += len(r1) - len(r2)

print 'answer: {}'.format(answer) # 743
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~
