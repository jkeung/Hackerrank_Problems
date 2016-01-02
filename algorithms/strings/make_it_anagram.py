# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

first_word = raw_input()
second_word = raw_input()

first_dict = defaultdict(int)
second_dict = defaultdict(int)

deletions = 0

for char in first_word:
    first_dict[char]+=1
    second_dict[char]+=0
for char in second_word:
    first_dict[char]+=0
    second_dict[char]+=1
    
for key in first_dict:
    deletions += abs(first_dict[key] - second_dict[key])

print deletions
