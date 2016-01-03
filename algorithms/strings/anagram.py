# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
t = int(raw_input())

def anagram(word):
    string_one = sorted(word[:len(word)/2])
    string_two = sorted(word[len(word)/2:])
    
    dict_one = defaultdict(int)
    dict_two = defaultdict(int)
    
    replacements = 0
    
    # if the string length is not the same return -1
    if len(string_one) != len(string_two):
        return -1
    
    # add the characters from both strings to corresponding dictionaries
    for i in range(len(string_two)):
        dict_one[string_one[i]]+=1
        dict_one[string_two[i]]+=0
        dict_two[string_one[i]]+=0
        dict_two[string_two[i]]+=1
            
    # if the number of characters differs for the strings add to a running count
    for key in dict_one:
        replacements+=abs(dict_one[key]-dict_two[key])
        
    # since there are two strings return have the number of differences
    return replacements/2

for i in range(t):
    print anagram(raw_input())
