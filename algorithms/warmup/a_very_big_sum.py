#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

summation = reduce(lambda x,y: x + y, arr, 0)
print summation
