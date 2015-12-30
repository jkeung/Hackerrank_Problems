# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())

for i in range(n):
    min_range, max_range = map(int, raw_input().split())
    count = 0
    curr = min_range
    num = int(curr**.5)
    while curr <= max_range:
        curr = num**2
        if min_range <= curr <= max_range:
            count+=1
        num+=1
    print count



