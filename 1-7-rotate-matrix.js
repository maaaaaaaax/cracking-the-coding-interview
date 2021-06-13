// 1.7 Rotate Matrix

// Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

even_matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

odd_matrix = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]
]

function validate_input(matrix)
{
    let length = matrix.length;
    let row_count = 0;
    for (let i = 0; i < length; i++)
    {
        if (matrix[i].length != length)
        {
            return false;
        }
        row_count++;
    }
    if (row_count != length)
    {
        return false;
    }
    else
    {
        return true;
    }
}

function rotate_matrix(matrix)
{
    if (!validate_input(matrix))
    {
        return "Error: Input matrix is not NxN";
    }
    let layers_left = Math.floor(matrix.length / 2);
    let layers_removed = 0;
    let next = matrix[0][0];
    let current = matrix[0][0]
    while (layers_removed < layers_left)
    {
        current = matrix[layers_removed][layers_removed];
        // Print the top row
        for (let i = 0 + layers_removed; i < ((matrix.length - layers_removed) - 1); i++)
        {
            next = matrix[0 + layers_removed][i + 1];
            matrix[0 + layers_removed][i + 1] = current;
            current = next;
            // console.log(matrix[0 + layers_removed][i]);
        }
        // Print a line break
        // console.log("");
        // Print the right column
        for (let row = 0 + layers_removed; row < (matrix.length - (1 + layers_removed)); row++)
        {
            next = matrix[row + 1][matrix.length - (1 + layers_removed)];
            matrix[row + 1][matrix.length - (1 + layers_removed)] = current;
            current = next;
            // console.log(matrix[row][matrix.length - (1 + layers_removed)]);
        }
        // Print a line break
        // console.log("");
        // Print the bottom row
        for (let column = matrix.length - (1 + layers_removed); column > (0 + layers_removed); column--)
        {
            next = matrix[matrix.length - (1 + layers_removed)][column - 1]
            matrix[matrix.length - (1 + layers_removed)][column - 1] = current;
            current = next;
            // console.log(matrix[matrix.length - (1 + layers_removed)][column]);
        }
        // Print a line break
        // console.log("");
        // Print the left column
        for (let row = matrix.length - (1 + layers_removed); row > (0 + layers_removed); row--)
        {
            next = matrix[row - 1][0 + layers_removed];
            matrix[row - 1][0 + layers_removed] = current;
            current = next;
            // console.log(matrix[row][0 + layers_removed])
        }
        // Print a line break
        // console.log("");
        layers_removed++;
    }
    return matrix;
}

console.log(rotate_matrix(even_matrix));
console.log("");
console.log(rotate_matrix(odd_matrix));
