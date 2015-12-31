#!/bin/python

import sys

n = int(raw_input().strip())
grid = []
for _ in xrange(n):
    row = str(raw_input().strip())
    grid.append(row)
    
length = len(grid)

for i in range(length):
    s = ''
    for j in range(length):
        if (i==0 or i==length-1 or j==0 or j==length-1):
            s+=grid[i][j]
        elif grid[i][j] > grid[i-1][j] and \
            grid[i][j] > grid[i+1][j] and \
            grid[i][j] > grid[i][j-1] and \
            grid[i][j] > grid[i][j+1]:
            s+='X'
        else:
            s+=grid[i][j]
    print s
