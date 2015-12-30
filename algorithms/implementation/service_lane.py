#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
    i,j = map(int,raw_input().strip().split(' '))
    min_size = width[i]
    for size in range(i, j+1):
        if width[size] < min_size:
            min_size = width[size]
    print min_size
