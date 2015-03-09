from math import sqrt
from math import log10

Phi = (1+sqrt(5))/2
phi = (1-sqrt(5))/2

n = 4782
print n*log10(Phi) - log10(sqrt(5))
