# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

def palindrome_check(string):
    mid = len(string)/2
    if len(string)%2==1:
        front = string[:mid+1]
    else:
        front = string[:mid]
        
    back = string[mid:]
    if front == back[::-1]:
        return True
    return False

def remove_index(string):
    for i in range(len(string)):
        if palindrome_check(string[:i]+string[i+1:]):
            return i
    return -1
    
for i in range(t):
    print remove_index(raw_input())
