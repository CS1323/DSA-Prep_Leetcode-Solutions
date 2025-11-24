def transpose(matrix):

    ROWS, COLS = len(matrix), len(matrix[0])
    transposed = [[0] * ROWS for _ in range(COLS)]

    for r in range(ROWS):
        for c in range(COLS):
                transposed[c][r] = matrix[r][c]

    return transposed

    # Time:  O(m*n)
    # Space: O(m*n)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3],[4,5,6]]
print(transpose(matrix))