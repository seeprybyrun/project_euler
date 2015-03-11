# -*- coding: utf-8 -*-
# In England the currency is made up of pound, £, and pence, p, and there
# are eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

import itertools

def flatten(listOfLists):
    "Flatten one level of nesting"
    return [x for x in itertools.chain.from_iterable(listOfLists)]

##splits = { '5v': ['2p+2p+1p','2p+1p+1p+1p','1p+1p+1p+1p+1p'],
##           '10v': ['5p+5p','5p+5v'] +
##           ['+'.join(['2p']*(5-k) + ['1p+1p']*k) for k in range(6)],
##           '20v': ['10p+10p','10p+10v'] +
##           ['+'.join(['5p']*(4-k) + ['5v']*k) for k in range(4)] +
##           ['+'.join(['2p']*(50-k) + ['1p+1p']*k) for k in range(11)],
##           '50v': ['20p+20p+10p','20p+20p+10v'] +
##           ['20p+10p+10p+10v','20p+10p+10v+10v','20p+10v+10v+10v'] +
##           ['+'.join(['10p']*(5-k) + ['10v']*k) for k in range(5)] +
##           ['+'.join(['5p']*(10-k) + ['5v']*k) for k in range(10)] +
##           ['+'.join(['2p']*(20-k) + ['1p+1p']*k) for k in range(21)],
##           '100v': ['50p+50p','50p+50v'] +
##           ['+'.join(['20p']*(5-k) + ['20v']*k) for k in range(5)] +
##           ['+'.join(['10p']*(10-k) + ['10v']*k) for k in range(10)] +
##           ['+'.join(['5p']*(20-k) + ['5v']*k) for k in range(20)] +
##           ['+'.join(['2p']*(50-k) + ['1p+1p']*k) for k in range(51)],
##           '200v': ['200p','100p+100p','100p+100v'] +
##           ['+'.join(['50p']*(4-k) + ['50v']*k) for k in range(4)] +
##           ['+'.join(['20p']*(10-k) + ['20v']*k) for k in range(10)] +
##           ['+'.join(['10p']*(20-k) + ['10v']*k) for k in range(20)] +
##           ['+'.join(['5p']*(50-k) + ['5v']*k) for k in range(50)] +
##           ['+'.join(['2p']*(100-k) + ['1p+1p']*k) for k in range(101)] }

splits = { '5v': ['2+2+1','2+1+1+1','1+1+1+1+1'],
           '10v': ['5+5','5+5v'] +
           ['+'.join(['2']*(5-k) + ['1+1']*k) for k in range(6)],
           '20v': ['10+10','10+10v'] +
           ['+'.join(['5']*(4-k) + ['5v']*k) for k in range(4)] +
           ['+'.join(['2']*(50-k) + ['1+1']*k) for k in range(11)],
           '50v': ['20+20+10','20+20+10v'] +
           ['20+10+10+10v','20+10+10v+10v','20+10v+10v+10v'] +
           ['+'.join(['10']*(5-k) + ['10v']*k) for k in range(5)] +
           ['+'.join(['5']*(10-k) + ['5v']*k) for k in range(10)] +
           ['+'.join(['2']*(20-k) + ['1+1']*k) for k in range(21)],
           '100v': ['50+50','50+50v'] +
           ['+'.join(['20']*(5-k) + ['20v']*k) for k in range(5)] +
           ['+'.join(['10']*(10-k) + ['10v']*k) for k in range(10)] +
           ['+'.join(['5']*(20-k) + ['5v']*k) for k in range(20)] +
           ['+'.join(['2']*(50-k) + ['1+1']*k) for k in range(51)],
           '200v': ['200','100+100','100+100v'] +
           ['+'.join(['50']*(4-k) + ['50v']*k) for k in range(4)] +
           ['+'.join(['20']*(10-k) + ['20v']*k) for k in range(10)] +
           ['+'.join(['10']*(20-k) + ['10v']*k) for k in range(20)] +
           ['+'.join(['5']*(50-k) + ['5v']*k) for k in range(50)] +
           ['+'.join(['2']*(100-k) + ['1+1']*k) for k in range(101)] }

def make_change(s):
    coins = s.split('+')
    #print coins
    for i,c in enumerate(coins):
        if 'v' not in c: # denotes a terminal
            coins[i] = [c]
        else:
            coins[i] = flatten(map(make_change,splits[c]))
            #print coins[i]
    # do a traversal of the tree (represented as nested lists?)
    #return coins
    
    # choose one string from each element and join them together with '+'
    return ['+'.join(x) for x in itertools.product(*coins)]

print make_change('50v')
