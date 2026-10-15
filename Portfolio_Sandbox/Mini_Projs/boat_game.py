def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    
    positions = [from_row, from_column, to_row, to_column]
    
    for pos in positions:
        if not isinstance(pos, int):
            return('Inputs not integers - rerun function')
        if pos > 5:
            return('False, Out of bounds') # make more robust
    
    if game_matrix[from_row][from_column] == False:
        return('Invalid start point on map - rerun function')
    
    # get vertical difference and horizontal difference
    vert_dist = from_row - to_row # if positive, going up
    if vert_dist == 0:
        pass
    elif vert_dist > 0: # going up 
        count = 1
        while count <= vert_dist:
            if game_matrix[from_row + count][from_column] == True:
                count += 1
                continue
            else:
                return("False, can't travel through land")
    else: # going down
        count = 1
        while count <= vert_dist:
            if game_matrix[from_row - count][from_column] == True:
                count += 1
                continue
            else:
                return("False, can't travel through land")
    
    hor_dist = from_column - to_column # if positive, going to the left 
    
    if hor_dist == 0:
        pass
    elif hor_dist > 0: 
        count = 1
        while count <= hor_dist:
            if game_matrix[from_row][from_column + count] == True:
                count += 1
                continue
            else:
                return("False, can't travel through land")
    else: # we move to the right
        count = from_column - 1
        while count > hor_dist:
            if game_matrix[from_row][from_column - count] == True:
                count -= 1
                continue
            else:
                return("False, can't travel through land")
        
    # Check the to position to see if it's land
    if game_matrix[to_row][to_column] == False:
        return('Invalid move - cannot move to land spot!')
        
    else:
        return('True, Valid move')
    
''' 
A working answer  
def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    rows = len(game_matrix)
    cols = len(game_matrix[0])

    # bounds check for both points (includes negatives)
    for r, c in ((from_row, from_column), (to_row, to_column)):
        if not (0 <= r < rows and 0 <= c < cols):
            return False

    # straight lines only (adjust if diagonals are allowed)
    if from_row != to_row and from_column != to_column:
        return False

    # direction of travel: -1, 0, or 1
    row_step = (to_row > from_row) - (to_row < from_row)
    col_step = (to_column > from_column) - (to_column < from_column)

    r, c = from_row, from_column
    while (r, c) != (to_row, to_column):
        r += row_step
        c += col_step
        if not game_matrix[r][c]:   # land in the way, or destination is land
            return False

    return True
'''

if __name__ == "__main__":
    game_matrix = [
        [False, True,  True,  False, False, False],
        [True,  True,  True,  False, False, False],
        [True,  True,  True,  True,  True,  True],
        [False, True,  True,  False, True,  True],
        [False, True,  True,  True,  False, True],
        [False, False, False, False, False, False],
    ]

    print(can_travel_to(game_matrix, 3, 2, 2, 2))
    # (can_travel_to(game_matrix, 3, 2, 2, 2)) # True, Valid move
    print(can_travel_to(game_matrix, 3, 2, 3, 4)) # False, Can't travel through land
    print(can_travel_to(game_matrix, 3, 2, 6, 2)) # False, Out of bounds