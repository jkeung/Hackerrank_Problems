#!/bin/python
from __future__ import division
import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos = []
neg = []
zero = []

for num in arr:
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero.append(num)
        
print len(pos) / len(arr)
print len(neg) / len(arr)
print len(zero) / len(arr)