#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    num_chocolates = 0
    wrappers = 0
    
    while n/c>0 or wrappers/m > 0:
        if n/c>0:
            num_chocolates += n / c
            n -= num_chocolates * c
            wrappers += num_chocolates
        if wrappers / m >= 1:
            bonus_chocolates = wrappers / m
            num_chocolates += bonus_chocolates
            wrappers = wrappers % m + bonus_chocolates
        
    print num_chocolates
