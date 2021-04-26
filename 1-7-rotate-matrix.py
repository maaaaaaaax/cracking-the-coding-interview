# 1.7 Rotate Matrix

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

matrix = [
    [  0,   1,    2,   3 ],
    [  4,   5,    6,   7 ],
    [  8,   9,   10,  11 ],
    [ 12,  13,   14,  15 ]
]

for i in matrix:
    print(i)

# Output:
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]