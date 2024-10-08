number_of_rows, number_of_columns = map(int, input().split())
current_matrix = []
my_pos = []
oponents = 0
moves = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(number_of_rows):
    row_data = input().split()
    current_matrix.append(row_data)

    if "B" in row_data:
        my_pos = [row, row_data.index("B")]
        current_matrix[row][my_pos[1]] = "-"

direction = input()

while direction != "Finish" and oponents < 3:

    r = directions[direction][0] + my_pos[0]
    c = directions[direction][1] + my_pos[1]
    if 0 <= r < number_of_rows and 0 <= c < number_of_columns:
        if current_matrix[r][c] == "P":
            current_matrix[r][c] = "-"
            oponents += 1
            moves += 1
            my_pos = [r, c]
        elif current_matrix[r][c] == "-":
            moves += 1
            my_pos = [r, c]
    direction = input()

print(f"Game over!")
print(f'Touched opponents: {oponents} Moves made: {moves}')
