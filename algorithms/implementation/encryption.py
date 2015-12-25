#!/bin/python

import sys
import math

s = raw_input().strip()

rows = int(math.floor(math.sqrt(len(s))))
cols = int(math.ceil(math.sqrt(len(s))))
matrix = []

for i in range(rows+1):
    start = i * cols
    end = min((i+1)*cols,len(s))
    matrix.append(s[start:end])
    
output_list = []
for i in range(cols):
    text = ''
    for word in matrix:
        try:
            text+=word[i]
        except:
            pass
    output_list.append(''.join(text))
    
print ' '.join(output_list)
