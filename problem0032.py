# -*- coding: utf-8 -*-
# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
# 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

import itertools
import time

start_time = time.clock()

prods = set()

symbols = ['1','2','3','4','5','6','7','8','9','*','==']
for x in itertools.permutations(symbols):
    if not(1 <= x.index('*') <= 4) or x.index('==') != 6:
        continue
    first_num_starts_with = int(x[0])
    second_num_starts_with = int(x[x.index('*')+1])
    if first_num_starts_with > second_num_starts_with:
        continue
    if first_num_starts_with * second_num_starts_with > 9:
        continue
    first_num = int(''.join(x[0:x.index('*')]))
    second_num = int(''.join(x[x.index('*')+1:6]))
    third_num = int(''.join(x[7:]))
    #formula = ''.join(x)
    #if eval(formula):
    if first_num * second_num == third_num:
        print '{0}*{1}=={2}'.format(first_num,second_num,third_num)
        prods.add(third_num)
        
#print prods
print sum(prods)

end_time = time.clock()
print "{0} seconds elapsed".format(end_time - start_time)
