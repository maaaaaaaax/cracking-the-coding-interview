#  1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

matrix = [
    [1, 0, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4]
]

def zero_matrix(matrix):

    # Create a new matrix of the same size, to avoid overwriting data
    rows = len(matrix)
    columns = len(matrix[0])
    new_matrix = []
    for row in range(0, rows):
        row_data = []
        for column in range(0, columns):
            row_data.append(1)
        new_matrix.append(row_data)

    # Iterate through each index of each row of the given matrix. 
    # If the value of the index is 0, set the value of each index in that row of the new_matrix to 0, then continue on to the new row
    for row in range(0, rows):
        for index in range(0, columns):
            if matrix[row][index] == 0:
                for cell in range(0, columns):
                    new_matrix[row][cell] = 0
                continue

    # Iterate through each index of each column of the given matrix. 
    # If the value of the index is 0, set the value of each index in that column of the new_matrix to 0, then continue on to the new column
    for column in range(0, columns):
        for row in range(0, rows):
            if matrix[row][column] == 0:
                for cell in range(0, rows):
                    new_matrix[cell][column] = 0
                continue

    # Iterate through the new matrix. If the cell is a 1, replace the value with the original value
    for row in range(0, rows):
        for cell in range(0, columns):
            if new_matrix[row][cell] == 1:
                new_matrix[row][cell] = matrix[row][cell]

    # Print the new matrix as a sanity check
    # for row in new_matrix:
    #     print(row)

    return new_matrix

zeroed_matrix = zero_matrix(matrix)
for row in zeroed_matrix:
    print(row)

# Output:
# [0, 0, 0, 0]
# [1, 0, 1, 1]
# [1, 0, 1, 1]