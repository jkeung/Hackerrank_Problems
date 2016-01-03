# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
t = int(raw_input())

def anagram_combinations(string):
    combinations = 0
    d = defaultdict(int)
    for l in range(1, len(string)+1):
        for i in range(len(string)-l+1):
            sub = ''.join(sorted(string[i:i+l]))
            d[sub]+=1
            # for every substring add to the running total of combinations
            combinations+=d[sub]-1

    return combinations
            
for i in range(t):
    print anagram_combinations(raw_input())
        
