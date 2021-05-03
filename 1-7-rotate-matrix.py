# 1.7 Rotate Matrix

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

import math

even_matrix = [
    [   0,    1,      2,     3 ],
    [   4,    5,      6,     7 ],
    [   8,    9,    10,   11 ],
    [ 12,  13,    14,  15  ]
]

odd_matrix = [
    [    0,      1,     2,     3,      4 ],
    [    5,      6,     7,     8,      9 ],
    [  10,    11,   12,   13,   14 ],
    [  15,    16,   17,   18,   19 ],
    [  20,    21,   22,   23,   24 ]
]

def rotate_matrix(matrix):

    # Create a new matrix so we don't overwrite original data
    length = len(matrix)
    new_matrix = []
    for row in range(0, length):
        row_data = []
        for column in range(0, length):
            row_data.append(0)
        new_matrix.append(row_data)

    # Set a variable to track the length of the current matrix
    i = len(matrix)

    # Remove one layer of the onion at a time
    while i > 1:
        # J tracks the layer of the onion. The outside of the onion is 0.
        j = 0
        while j < i:

            # Rotate the first row
            for k in range(0, i - 1):
                new_matrix[j][k+j+1] = matrix[j][k+j]
            
            # Rotate the last column
            for k in range(0, i - 1):
                new_matrix[j + k + 1][i - 1 + j] = matrix[j + k][i - 1 + j] 
            
            # Rotate the last row
            for k in reversed(range(1, i)):
                new_matrix[i - 1 + j][k+j - 1] = matrix[i - 1 + j][k+j]
            
            # Rotate the first column
            for k in reversed(range(1, i)):
                new_matrix[k + j - 1][0 + j] = matrix[k + j][0 + j]
            if i % 2 == 0:
                i = i / 2
            elif math.floor((i / 2)) == 1:
                i = 1
            else:
                i = int(math.floor((i / 2)) + 1)
            if i == 1 and length % 2 == 1:
                center = int(math.floor((length / 2)))
                new_matrix[center][center] = matrix[center][center]
            j += 1
    return new_matrix

print(rotate_matrix(even_matrix))