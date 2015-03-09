import re
from decimal import *
from math import log10
from math import floor

prec = 2000
getcontext().prec = prec
best = {'d':-1,
        'group':None,
        'len':741}
for d in range(1,1000):
##    while d % 2 == 0:
##        d = d/2
##    while d % 5 == 0:
##        d = d/5
    if d % 100 == 0:
        print d
    for k in range(prec/2,best['len'],-1):
        pattern_str = "(?P<grp>.{" + str(k) + "})(?P=grp)"
        pattern = re.compile(pattern_str)
    
        digits = floor(log10(d))+1
        s = repr(Decimal(10**(digits-1))/Decimal(d))
        match = pattern.search(s)

        if match:
            pattern2 = re.compile("(?P<grp>.+)(?P=grp)")
            while match:
                group = match.group(1)
                match = pattern2.match(group)
            #print "{0}: {1}".format(d,group)
            if len(group) > best['len']:
                best['d'] = d
                best['group'] = group
                best['len'] = len(group)
            break

print "best match is {0}: {1}".format(best['d'],best['group'])
