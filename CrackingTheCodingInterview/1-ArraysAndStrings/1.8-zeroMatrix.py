# helper
def printMatrix(matrix):
    for r in matrix:
        for c in r:
            print(c, end='\t')
        print('\n')
    print("-" * 32)

# time: O(m*n), space: O(m+n)
def zeroMatrix(matrix):
    rows = cols = []
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for i in rows:
        for j in range(n):
            matrix[i][j] = 0
    for j in cols:
        for i in range(m):
            matrix[i][j] = 0

    return matrix

matrix = [
    [0, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

printMatrix(matrix)
printMatrix(zeroMatrix(matrix))