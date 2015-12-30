#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    count = 0
    for char in str(n):
        denom = float(char)
        # make sure no divide by zero and digit perfectly divides number
        if denom != 0 and n % denom == 0:
            count +=1
            
    print count
