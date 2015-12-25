#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    num_fives = 0
    num_threes = 0


    for i in range(0,n + 1,5):
        
        if (n - i) % 3 == 0:
            num_threes = i
            num_fives = n - i
            break

    if num_fives + num_threes == n:
        print '5' * num_fives + '3' * num_threes
    else:
        print '-1'
