#!/bin/python

import sys


n = int(raw_input().strip())

def factorial(num):
    if num==1:
        return 1
    elif num<=0:
        return -1
    else:
        return num * factorial(num-1)

print factorial(n)
