def read_matrix_func():
    number_of_rows, number_of_columns = map(int, input().split(', '))
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix_func()
matrix_elements_sum = 0

for i in range(len(matrix)):
    current_row = matrix[i]
    matrix_elements_sum += sum(current_row)

print(matrix_elements_sum)
print(matrix)