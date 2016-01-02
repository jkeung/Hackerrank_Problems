# Enter your code here. Read input from STDIN. Print output to STDOUT

m,n,rotations = map(int, raw_input().split())
matrix = []
for i in range(m):
    row = raw_input().split()
    matrix.append(row)
    

def rotate_matrix(matrix):
    top = 0
    left = 0
    right = n-1
    bottom = m-1

    while top < bottom and left < right:
        
        prev = matrix[top][left]
        
        for i in range(left, right):
            matrix[top][i] = matrix[top][i+1]
        
        for i in range(top, bottom):
            matrix[i][right] = matrix[i+1][right]
        
        for i in range(right, left, -1):
            matrix[bottom][i] = matrix[bottom][i-1]
        
        for i in range(bottom, top, -1):
            matrix[i][left] = matrix[i-1][left]
        
        matrix[top+1][left] = prev
        
        top+=1
        right-=1
        bottom-=1
        left+=1
        
        
def print_matrix(matrix):
    for row in matrix:
        print ' '.join(row)

for i in range(rotations):
    rotate_matrix(matrix)
print_matrix(matrix)
