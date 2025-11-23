def setZeroes(matrix):

    ROWS, COLS = len(matrix), len(matrix[0])
    row_zero = False    # row 0 contains a 0

    # determine which rows/cols need to be zero
    for r in range(ROWS):
        for c in range(COLS):

            if matrix[r][c] == 0:
                matrix[0][c] = 0

                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True

    # zero rows/cols
    for r in range(1, ROWS):
        for c in range(1, COLS):

            if matrix [r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    
    # zero col 0
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    # zero row 0
    if row_zero:
        for c in range(COLS):
            matrix[0][c] = 0

    return

    # Time:  O(m*n)
    # Space: O(1)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(matrix)
setZeroes(matrix)
print(matrix)