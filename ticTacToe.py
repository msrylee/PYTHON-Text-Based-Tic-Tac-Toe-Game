#Lab 10
#Rylee Price

def buildBoard():
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    return board_list

def displayBoard(a_list):
    print(a_list[0], "|", a_list[1], "|", a_list[2])
    print("---------")
    print(a_list[3], "|", a_list[4], "|", a_list[5])
    print("---------")
    print(a_list[6], "|", a_list[7], "|", a_list[8])

def isLegal(board, spot):
    if isinstance(board[spot - 1], int):
        result = True
    else:
        result = False

    return result

def fillSpot(board, spot, char):
    if isLegal(board, spot):
        board[spot - 1] = char

def isGameWon(board):
    #Checking diagonal win (top right to bottom left)
    if (board[2] == "x") and (board[4] == "x") and (board[6] == "x"):
        result = True
    elif (board[2] == "o") and (board[4] == "o") and (board[6] == "o"):
        result = True
    #Checking diagonal win (top left to bottom right)
    elif (board[0] == "x") and (board[4] == "x") and (board[8] == "x"):
        result = True
    elif (board[0] == "o") and (board[4] == "o") and (board[8] == "o"):
        result = True
    #Checking left column win
    elif (board[0] == "x") and (board[3] == "x") and (board[6] == "x"):
        result = True
    elif (board[0] == "o") and (board[3] == "o") and (board[6] == "o"):
        result = True
    #Checking center column win
    elif (board[1] == "x") and (board[4] == "x") and (board[7] == "x"):
        result = True
    elif (board[1] == "o") and (board[4] == "o") and (board[7] == "o"):
        result = True
    #Checking right column win
    elif (board[2] == "x") and (board[5] == "x") and (board[8] == "x"):
        result = True
    elif (board[2] == "o") and (board[5] == "o") and (board[8] == "o"):
        result = True
    #Checking top row win
    elif (board[0] == "x") and (board[1] == "x") and (board[2] == "x"):
        result = True
    elif (board[0] == "o") and (board[1] == "o") and (board[2] == "o"):
        result = True
    #Checking middle row win
    elif (board[3] == "x") and (board[4] == "x") and (board[5] == "x"):
        result = True
    elif (board[3] == "o") and (board[4] == "o") and (board[5] == "o"):
        result = True
    #Checking bottom row win
    elif (board[6] == "x") and (board[7] == "x") and (board[8] == "x"):
        result = True
    elif (board[6] == "o") and (board[7] == "o") and (board[8] == "o"):
        result = True
    else:
        result = False

    return result

def isGameOver(board, numPlays):
    if isGameWon(board) or numPlays >= 9:
        result = True
    else:
        result = False

    return result

def playGame():
    print("This program runs a game of Tic-Tac-Toe")
    print()

    numPlays = 0
    player_number = 1
    char = ""
    
    board_list = buildBoard()

    displayBoard(board_list)

    print()

    user_entry = input("Hit <Enter> to start the game. Hit any other key to exit.")

    while user_entry == "":
        print(f"Player {player_number}'s turn")
        print()
        spot = int(input("Enter a spot on the board to fill: "))
        print()

        if player_number == 1:
            char = "x"
        if player_number == 2:
            char = "o"
        
        fillSpot(board_list, spot, char)

        numPlays += 1

        print(numPlays)
            
        displayBoard(board_list)
        print()

        if player_number == 1:
            player_number = 2
        elif player_number == 2:
            player_number = 1

        if isGameOver(board_list, numPlays):
            print("Game over.")
            break
        else:
            user_entry = input("This turn is over. Hit <Enter> to start the next turn. Hit any other key to exit.")
def main():
    playGame()

if __name__ == "__main__":
    main()
