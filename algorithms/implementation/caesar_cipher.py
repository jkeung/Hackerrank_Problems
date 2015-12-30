#!/bin/python

import sys
import string

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

text = ''
for char in s:
    if char in string.lowercase:
        text+=string.lowercase[(string.lowercase.find(char) +k) % 26]
    elif char in string.uppercase:
        text+=string.uppercase[(string.uppercase.find(char) +k) % 26]
    else:
        text+=char
print text
