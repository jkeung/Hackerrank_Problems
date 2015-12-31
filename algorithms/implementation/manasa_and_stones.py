# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for _ in range(t):
    n,a,b = [int(raw_input()) for _ in range(3)]
    outputs = []
    for i in range(n):
        outputs.append((n-1-i)*a + (i)*b)
    outputs = list(set(outputs))
    for num in sorted(outputs):
        print num,
    print
    
