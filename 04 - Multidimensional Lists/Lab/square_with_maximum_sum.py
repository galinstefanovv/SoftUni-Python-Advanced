# read matrix sizes from the console
rows, columns = map(int, input().split(", "))

# initialize the matrix with zeros
matrix = [[0 for j in range(columns)] for i in range(rows)]

# read matrix elements from the console
for i in range(rows):
    row_elements = input().split(", ")
    for j in range(columns):
        matrix[i][j] = int(row_elements[j])

# initialize variables to track the maximum sum and the corresponding submatrix
max_sum = None
max_submatrix = None

# iterate over all 2x2 submatrices in the top-left corner of the matrix
for i in range(rows-1):
    for j in range(columns-1):
        submatrix_sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
        if max_sum is None or submatrix_sum > max_sum:
            max_sum = submatrix_sum
            max_submatrix = [[matrix[i][j], matrix[i][j+1]], [matrix[i+1][j], matrix[i+1][j+1]]]

# print the maximum submatrix and its sum
for row in max_submatrix:
    print(" ".join(str(elem) for elem in row))
print(max_sum)