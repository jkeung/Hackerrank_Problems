# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
t = int(raw_input())

def substring(string_one, string_two):
    dict_one = defaultdict(int)
    dict_two = defaultdict(int)
    
    for char in string_one:
        dict_one[char]+=1
        
    for char in string_two:
        if char in dict_one:
            return 'YES'
    return 'NO'
    
for i in range(t):
    print substring(raw_input(), raw_input())
