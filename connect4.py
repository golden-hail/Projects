def connect4():
    # Starting state: empty board, player 1 goes first
    board = [["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"]]
    sep = '----------------------------------------'
    col_labels = '  0    1    2    3    4    5    6    7  <--- column numbers'
    
    player = 'PLAYER 1'
    token = 'x'
    
    hor_win = 0
    vert_win = 0
    game_won = 0
    col_height = [0, 0, 0, 0, 0, 0, 0, 0]
    valid_move = False
    
    print(sep)
    print("               CONNECT 4")
    
    def display_board():
        # set up the board!
        print(sep)
        print(sep)
        for collection in board:
            for slot in collection:
                print("  " + slot, end="  ")
            print()
        print(sep)
        print(col_labels)
        print(sep)
    
    # Game time!
    while game_won == 0:
        display_board()

        # check if input 'slot_in' is a valid input 
        while valid_move == False:
            bot_row = 6
            slot_in = input(f"Your move {player} - Select a slot 0-7: " )
            
            try:
                slot_in = int(slot_in)
                bot_row = 6
                if slot_in > 7: # check if slot exists (only 0-7 exists)
                    display_board()
                    print(f"{slot_in} is greater than 7. Let's try again!")
                elif col_height[slot_in] > 6: # check if the column of slot_in is full
                    display_board()
                    print(f"Column {slot_in} is full. Let's try again!")
                else:
                    valid_move = True
            except:
                if isinstance(slot_in, int) == False:
                    display_board()    
                    print(f"Your input, '{slot_in}' is not a number. Let's try again!")
                    
        # clear valid_move check so that the check goes off on the next loop
        valid_move = False
        
        # find the correct row to place the token into      
        while board[bot_row][slot_in] != "0":
            bot_row -= 1
        
        # place the token
        board[bot_row][slot_in] = token
    
        col_height[slot_in] += 1
        
        # check for horozontal win 
        # for each inner array for the board (ie the rows)
        for inner_array in board:
            # for each index in each row array (inner_array)
            for slot in inner_array:
                if slot == token:
                    hor_win += 1                
                else:
                    hor_win = 0
                if hor_win == 4:
                    game_won = 1
    
        # check vertical win
        if col_height[slot_in] >= 4:
            # check with a for loop if each row of the column holds the same token type
            for inner_array in board:
                if inner_array[slot_in] == token:
                    vert_win += 1
                else:
                    vert_win = 0
                if vert_win == 4:
                    game_won = 1
    
        # check diagonal win
        # diag_down win check
        for inner_array in board:
            if game_won == 1:
                break
            
            for slot in inner_array:
                if slot == token:
                    array_idx = board.index(inner_array)
                    slot_idx = inner_array.index(slot)
                    try:
                        # if diag down is a win
                        if board[array_idx+1][slot_idx+1] == token and board[array_idx+2][slot_idx+2] == token and board[array_idx+3][slot_idx+3] == token:
                            game_won = 1
                        elif board[array_idx-1][slot_idx-1] == token and board[array_idx-2][slot_idx-2] == token and board[array_idx-3][slot_idx-3] == token:
                            game_won = 1
                    except:
                        pass
                        
                    try: 
                        # if diagonal up is a win
                        if board[array_idx+1][slot_idx-1] == token and board[array_idx+2][slot_idx-2] == token and board[array_idx+3][slot_idx-3] == token:
                            game_won = 1
                        elif board[array_idx-1][slot_idx+1] == token and board[array_idx-2][slot_idx+2] == token and board[array_idx-3][slot_idx+3] == token:
                            game_won = 1
                    except:
                        pass
    
        if game_won == 1:
            display_board() 
            print(f'Congratulations {player}, you won!')
            print(sep)
            replay = input("Would you like to have a rematch?: ")
            breakpoint()
            if replay.upper() == "YES" or replay.upper() == "Y": 
                connect4() 
            else:
                print(sep)
                print("Thanks for playing!")
                print(sep)
            break
    
        # switch player, then start the next turn 
        if player == 'PLAYER 1':
            player = 'PLAYER 2'
            token = 's'
        else:
            player = 'PLAYER 1'
            token = 'x'       

connect4()

# to do
    # color code console outputs?