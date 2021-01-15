# Given an image represented by an N*N matrix, where each pixel in the image is represented by an integer, 
# write a method to rotate the image by 90 degrees. 
# Can you do this in place?

# helper
def printMatrix(matrix):
    for r in matrix:
        for c in r:
            print(c, end='\t')
        print('\n')
    print("-" * 32)

# time: O(n^2), space: O(1)
def rotateMatrix1(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return False

    edge = n - 1

    for i in range(n // 2):
        for j in range(i, edge - i):
            temp                        = matrix[i][j]
            matrix[i][j]                = matrix[edge - j][i]
            matrix[edge - j][i]         = matrix[edge - i][edge - j]
            matrix[edge - i][edge - j]  = matrix[j][edge - i]
            matrix[j][edge - i]         = temp

    return matrix

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

printMatrix(matrix)
printMatrix(rotateMatrix1(matrix))