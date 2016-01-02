from collections import defaultdict

string = raw_input()
evens = 0
odds = 0
letter_dict = defaultdict(int)

for char in string:
    letter_dict[char] += 1
    
for value in letter_dict.values():
    if value%2 == 0:
        evens+=1
    else:
        odds+=1

if odds>1:
    print("NO")
else:
    print("YES")

