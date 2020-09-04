
# esma tyo repeat wala error cha need to fix the bug


board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9",]

def display_board():
        print( board[0] + "|",board[1] + "|",board[2] + "|")
        print( board[3] + "|",board[4] + "|",board[5] + "|")
        print( board[6] + "|",board[7] + "|",board[8] + "|")
        

# display_board()

game_on = True
winner = None
current_player="X"
counter = 0


def play_game():

    display_board()
    while game_on:
        turn_handler(current_player)
        change_player()
        check_game()
        

    if winner == "X" or winner == "O":
        print("\nThe winner is " + winner)   
    else:
        print("TIE")



def turn_handler(player):
    global counter

    position = input("Enter the position 1-9 ( "+player+" ) : ")


    # value = False
    # while not value :
    while int(position)<0 or int(position) >9:
        print("Invalid input.....\n")
        position = input("Enter the position 1-9 ( "+player+" ) : ")
        
    pos = int(position)-1
        # print(board[pos])

        # if board[pos] > -1 and board[pos] < 9:
        #     value = True
        #     break

        # else:
        #     print("Cannot override. Enter again")
        #     break      

    board[pos] = player   
    
    counter = counter + 1
        
    
    display_board()
    return counter



def check_game():
    check_win()
    check_tie()




def check_win():
    global winner
    row_winner = check_win_row()
    column_winner= check_win_col()
    diagonal_winner= check_win_dia()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None

    return



def check_win_row():
    global game_on
    if board[0]== board[1]== board[2]:
        game_on = False
        return board[0]

    elif board[3]== board[4]== board[5]:
        game_on = False
        return board[3]

    elif board[6]== board[7]== board[8]:
        game_on = False
        return board[6]

    return



def check_win_col():
    global game_on
    if board[0]== board[3]== board[6]:
        game_on = False
        return board[0]

    elif board[1]== board[4]== board[7]:
        game_on = False
        return board[1]

    elif board[2]== board[5]== board[8]:
        game_on = False
        return board[2]

    return



def check_win_dia():
    global game_on
    if  board[0]== board[4]== board[8]:
        game_on = False
        return board[0]
        
    if board[2]== board[4]== board[6]:
        game_on = False
        return board[2]
   
    return



def check_tie():
    global game_on
    global counter
    if counter == 9:
        game_on = False
    return



def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return



play_game()