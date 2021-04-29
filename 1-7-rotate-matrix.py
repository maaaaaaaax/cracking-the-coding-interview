# 1.7 Rotate Matrix

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

import math

even_matrix = [
    [  0,   1,    2,   3 ],
    [  4,   5,    6,   7 ],
    [  8,   9,   10,  11 ],
    [ 12,  13,   14,  15 ]
]

odd_matrix = [
    [   0,   1,    2,    3,    4 ],
    [   5,   6,    7,    8,    9 ],
    [  10,  11,   12,   13,   14 ],
    [  15,  16,   17,   18,   19 ],
    [  20,  21,   22,   23,   24 ]
]

# Output:
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]

# Start with a brute force, inefficient solution
def rotate_matrix(matrix):
    # Create a new matrix so we don't overwrite original data
    new_matrix = matrix
    i = len(matrix)
    while i > 1:
        j = 0
        while j < i:
            print('i: ' + str(i))
            print('j: ' + str(j))
            # Print first row
            for k in range(0, int(i)):
                print(matrix[j][k+j])
            # Print last column
            # Print last row, reversed 
            # Print first column, reversed
            j += 1
            if i % 2 == 0:
                i = i / 2
            if math.floor((i / 2)) == 1:
                i = 1
            else:
                i = math.floor((i / 2)) + 1

# Output:
# 4
# 0
# 1
# 2
# 3
# 5
# 6

rotate_matrix(odd_matrix)