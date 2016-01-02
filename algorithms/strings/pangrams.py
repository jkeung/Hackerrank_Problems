# Enter your code here. Read input from STDIN. Print output to STDOUT

import string
from collections import defaultdict
characters = string.lowercase
letter_dict = defaultdict(int)

sentence = raw_input().lower().replace(' ', '')

for char in sentence:
    letter_dict[char]+=1

if len(letter_dict)<26:
    print "not pangram"
else:
    print "pangram"
