#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr_sorted = sorted(arr)
min_cut = arr_sorted[0]

for i, num in enumerate(arr_sorted):
    if i == 0:
        print len(arr)
    elif num - min_cut <=0:
        pass
    else:
        print len(arr) - i
        min_cut = num

