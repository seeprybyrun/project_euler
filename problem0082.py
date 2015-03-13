# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
# the left column and finishing in any cell in the right column, and only moving
# up, down, and right, is equal to 994.
# 
# 131 673 234 103  18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331
# 
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
# As..."), a 31K text file containing a 80 by 80 matrix, from the left column
# to the right column.

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
answer = inf

print 'reading file'

##matrix = [[131,673,234,103, 18],
##          [201, 96,342,965,150],
##          [630,803,746,422,111],
##          [537,699,497,121,956],
##          [805,732,524, 37,331]]

f = open('data/p082_matrix.txt','r')
matrix = [ map(int,line.strip().split(',')) for line in f.readlines() ]
f.close()

print 'building vertex list'

# make vertex list
M = len(matrix)
N = len(matrix[0])
assert set([len(row) for row in matrix]) == set([N])
source = (-1,-1)
vertices = [ v for v in it.product(range(M),range(N)) ] + [source]

print 'building adjacency list'

# make adjacency list
neighbors = {v : [] for v in it.product(range(M),range(N))}
for i in range(M):
    for j in range(N):
        if j < N-1: # if not in last column, can move right
            neighbors[(i,j)] += [(i,j+1)]
        if i > 0: # if not in first row, can move up
            neighbors[(i,j)] += [(i-1,j)]
        if i < M-1: # if not in last row, can move down
            neighbors[(i,j)] += [(i+1,j)]
neighbors[source] = [(i,0) for i in range(M)]

print 'building weight function'

# weight of an edge is the value of the cell being entered
weight = { u : { v : matrix[v[0]][v[1]] for v in neighbors[u] } for u in vertices }

print 'computing shortest path'

dist,prev = dijkstra(vertices,neighbors,weight,source)
for i in range(M):
    answer = min(answer,dist[(i,N-1)])
        
print 'answer: {}'.format(answer) # 260324
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~5.83s
