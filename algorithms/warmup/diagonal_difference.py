#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
	a_temp = map(int,raw_input().strip().split(' '))
	a.append(a_temp)

x1 = reduce(lambda x,y:x+y,[a[i][i] for i in range(n)])
x2 = reduce(lambda x,y:x+y,[a[i][n-1-i] for i in range(n)])
print abs(x1 - x2)
