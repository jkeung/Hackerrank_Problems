# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

t = int(raw_input())
letter_dict = defaultdict(int)

for i in range(t):
    word = ''.join(set(raw_input()))
    for char in word:      
        letter_dict[char]+=1

print sum(1 for x in letter_dict.values() if x==t)

