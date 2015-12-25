#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, threshold = [int(n),int(k)]
    times = map(int,raw_input().strip().split(' '))
    num_on_time = len([time for time in times if time <= 0])
    if num_on_time >= threshold:
        print 'NO'
    else:
        print 'YES'
    
