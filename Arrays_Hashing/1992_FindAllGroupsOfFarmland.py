def findFarmland(land):

    ROWS, COLS = len(land), len(land[0])
    groups = []

    # find bottom right corner and add to group
    # -> ALL farmland groups are guaranteed to be solid rectangles
    def group_farmland(row, col):

        # bottom right cell (bott_row, bott_col)
        bott_row, bott_col = top_row, top_col = row, col

        # find bottom column (bott_col) -> go as far right
        while bott_col+1 < COLS and land[row][bott_col+1] == 1:
            bott_col += 1
            
        # find bottom row (bott_row) -> go as far down
        while bott_row+1 < ROWS and land[bott_row+1][col] == 1:
            bott_row += 1

        # set cells in group to visited (-1)
        for r in range(top_row, bott_row+1):
            for c in range(top_col, bott_col+1):
                land[r][c] = -1

        groups.append([top_row, top_col, bott_row, bott_col])

    # find top left cell to be grouped 
    for r in range(ROWS):
        for c in range(COLS):

            if land[r][c] == 1:
                group_farmland(r, c)
                
    return groups

    # Time:  O(m*n)
    # Space: O(1) -> no extra memory

land = [[1,0,0],
        [0,1,1],
        [0,1,1]]
print(findFarmland(land))