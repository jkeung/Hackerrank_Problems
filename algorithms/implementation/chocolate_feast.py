#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    num_chocolates = n/c
    wrappers = num_chocolates
    
    while wrappers >= m:
        bonus_chocolates = wrappers / m
        num_chocolates += bonus_chocolates
        wrappers = wrappers % m + bonus_chocolates
            
    print num_chocolates

