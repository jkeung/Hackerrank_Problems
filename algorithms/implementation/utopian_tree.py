#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    odd = True
    height = 1
    for cycle_num in range(1,n+1):
        if odd:
            height*=2
            odd = False
        else:
            height+=1
            odd = True
            
    print height

