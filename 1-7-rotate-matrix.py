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

# Output:
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]

# Start with a brute force, inefficient solution
def rotate_matrix(matrix):
    # Create a new matrix so we don't overwrite original data
    new_matrix = matrix[:]
    # Set a variable to track the length of the current matrix, removing one layer of the onion each iteration
    i = len(matrix)
    while i > 1:
        # J tracks the layer of the onion. The outside of the onion is 0.
        j = 0
        while j < i:
            print('\ni: ' + str(i))
            print('j: ' + str(j))
            # Print first row
            print("First row: ")
            for k in range(0, i - 1):
                print(matrix[j][k+j])
            # Print last column
            print("Last column: ")
            for k in range(0, i - 1):
                print(matrix[j + k][i - 1 + j]) 
            # Print last row, reversed
            print("Last row, reversed: ")
            for k in reversed(range(1, i)):
                print(matrix[i - 1 + j][k+j])
            # Print first column, reversed
            print("First column, reversed: ")
            for k in reversed(range(1, i)):
                print(matrix[k + j][0 + j])         
            j += 1
            if i % 2 == 0:
                i = i / 2
            elif math.floor((i / 2)) == 1:
                i = 1
            else:
                i = int(math.floor((i / 2)) + 1)

# Output:
# 4
# 0
# 1
# 2
# 3
# 5
# 6

rotate_matrix(odd_matrix)