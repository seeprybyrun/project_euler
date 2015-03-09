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
target = 988

try:
    print make_change(target,denoms)
except Exception as e:
    print e
