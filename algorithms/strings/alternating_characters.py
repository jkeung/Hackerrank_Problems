# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

def alt_chars(word):
    deletions = 0
    char = word[0]
    for i in range(1,len(word)):
        if word[i] == char:
            deletions+=1
        else:
            char = word[i]
    return deletions
        
for i in range(t):
    print alt_chars(raw_input())
    
