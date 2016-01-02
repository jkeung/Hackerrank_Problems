# Enter your code here. Read input from STDIN. Print output to STDOUT

m,n,rotations = map(int, raw_input().split())
matrix = []
for i in range(m):
    row = raw_input().split()
    matrix.append(row)
    

def rotate_matrix(matrix, rotations):
    top = 0
    left = 0
    right = n-1
    bottom = m-1
    
    while top < bottom and left < right:
        temp_list = []
        # extract outer circle of elements
        for i in range(left, right):
            temp_list.append(matrix[top][i])
        for i in range(top, bottom):
            temp_list.append(matrix[i][right])
        for i in range(right, left, -1):
            temp_list.append(matrix[bottom][i])
        for i in range(bottom, top, -1):
            temp_list.append(matrix[i][left])
        
        # move front elements to back
        rotate = rotations % len(temp_list)
        temp_list = temp_list[rotate:] + temp_list[:rotate]
        
        # reconstruct matrix
        for i in range(left, right):
            matrix[top][i] = temp_list.pop(0)
        for i in range(top, bottom):
            matrix[i][right] = temp_list.pop(0)
        for i in range(right, left, -1):
            matrix[bottom][i] = temp_list.pop(0)
        for i in range(bottom, top, -1):
            matrix[i][left] = temp_list.pop(0)
        
        top+=1
        right-=1
        bottom-=1
        left+=1
        
        
def print_matrix(matrix):
    for row in matrix:
        print ' '.join(row)


rotate_matrix(matrix, rotations)
print_matrix(matrix)