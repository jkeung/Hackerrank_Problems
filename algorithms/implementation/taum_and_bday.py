#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = map(int, raw_input().strip().split(' '))
    x,y,z = map(int, raw_input().strip().split(' '))

    x = min(x, y+z)
    y = min(y, x+z)
    total = b*x + w*y
    print total
