# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by only moving to the right and down, is equal to 2427.
# 
# 131 673 234 103  18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331
# 
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
# As..."), a 31K text file containing a 80 by 80 matrix, from the top left to
# the bottom right by only moving right and down.

import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy
import re

from math import floor,sqrt,log

inf = float('inf')

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def printByRow(matrix):
    for row in matrix:
        print row

def dijkstra(vertices,neighbors,weight,source):
    # dist[v] is the minimal distance from the source to v
    dist = {v: inf for v in vertices if v != source}
    dist[source] = 0

    # prev[v] is the previous node in an optimal path from
    # source to v
    prev = {v: None for v in vertices}
    
    # unprocessed nodes
    unvisited = set([v for v in vertices])

    while len(unvisited) > 0:
        u = min(unvisited,key=lambda v:dist[v]) # choose the smallest unvisited node
        unvisited.remove(u)
        for v in neighbors[u]: # for each neighbor of u...
            if v not in unvisited: continue # ...which is unvisited
            alternate = dist[u] + weight[u][v]
            if alternate < dist[v]: # decide whether going through u gives a better
                dist[v] = alternate # path to v
                prev[v] = u

    return dist,prev

factorial = [1,1,2,6,24,120,720,5040,40320,362880]

t0 = time.clock()
answer = 0

##matrix = [[131,673,234,103, 18],
##          [201, 96,342,965,150],
##          [630,803,746,422,111],
##          [537,699,497,121,956],
##          [805,732,524, 37,331]]

print 'reading file'

f = open('data/p081_matrix.txt','r')
matrix = [ map(int,line.strip().split(',')) for line in f.readlines() ]
f.close()

# idea: do Dykstra's algorithm on a digraph
# edge weight = value of the cell you enter
# source = top left
# sink = bottom right
# need to add value of source cell in order to account for no edges entering it

print 'building vertex list'

# make vertex list
M = len(matrix)
N = len(matrix[0])
assert set([len(row) for row in matrix]) == set([N])
vertices = [ v for v in it.product(range(M),range(N)) ]

print 'building adjacency list'

# make adjacency list
# for all cells in last column nor last row...
neighbors = { (i,j) : [(i+1,j),(i,j+1)] for (i,j) in vertices if i < M-1 and j < N-1 }
# for cells in last column not last row...
for i in range(M-1):
    neighbors[(i,N-1)] = [(i+1,N-1)]
# for cells in last row not last column...
for j in range(N-1):
    neighbors[(M-1,j)] = [(M-1,j+1)]
# for bottom-right cell...
neighbors[(M-1,N-1)] = []

print 'building weight function'

# weight of an edge is the value of the cell being entered
# nonexistent edges get a weight of infinity
weight = { u : { v : matrix[v[0]][v[1]] for v in neighbors[u] } for u in vertices }

# source is top-left cell, sink is bottom-right
source = (0,0)
sink = (M-1,N-1)

print 'computing shortest path'

dist,prev = dijkstra(vertices,neighbors,weight,source)
answer = matrix[source[0]][source[1]] + dist[sink]
        
print 'answer: {}'.format(answer) # 427337
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~5.61s
