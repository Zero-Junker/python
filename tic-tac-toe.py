
#Dictionary for the game
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

#Dictionary to show the value the player needs to type for each spot
moveBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'}
#All win conditions
def checkWin(turn):
    #horizontal
    if theBoard['1'] == turn and theBoard['2'] == turn and theBoard['3'] == turn:
        return True
    elif theBoard['4'] == turn and theBoard['5'] == turn and theBoard['6'] == turn:
        return True
    elif theBoard['7'] == turn and theBoard['8'] == turn and theBoard['9'] == turn:
        return True
    #vertical
    elif theBoard['1'] == turn and theBoard['4'] == turn and theBoard['7'] == turn:
        return True
    elif theBoard['2'] == turn and theBoard['5'] == turn and theBoard['8'] == turn:
        return True
    elif theBoard['3'] == turn and theBoard['6'] == turn and theBoard['9'] == turn:
        return True
    #Diagonal
    elif theBoard['1'] == turn and theBoard['5'] == turn and theBoard['9'] == turn:
        return True
    elif theBoard['3'] == turn and theBoard['5'] == turn and theBoard['7'] == turn:
        return True
    else:
        return False

#clear board
def clearBoard():
    theBoard['1'] = " "
    theBoard['2'] = " "
    theBoard['3'] = " "
    theBoard['4'] = " "
    theBoard['5'] = " "
    theBoard['6'] = " "
    theBoard['7'] = " "
    theBoard['8'] = " "
    theBoard['9'] = " "
    
#print game board
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

print("Welcome to Tic-Tac-Toe")
print("Here is the move board: ")
printBoard(moveBoard)
print()
print("Let's begin!")
print()
print()

turn = 'X'
playing = 'Y'
while playing == 'Y' or playing == 'y':
    printBoard(theBoard)
    for i in range(9):
        while True:
            #get move from player
            print('Turn for ' + turn + '. Move on which space?')
            print()
            move = input()

            if move in theBoard:
                if theBoard[move] == ' ':
                    theBoard[move] = turn
                    break
                else:
                     print("Invalid move please try again")
            else:
                print("Invalid move please try again")
        if checkWin(turn):
            print( turn + " wins!")
            print("would you like to play again (Y/N): ")
            playing = input("> ")
            while True:
                if playing == 'Y' or playing == 'y':
                    clearBoard()
                    break
                elif playing == 'N' or playing == 'n':
                    print("Thanks for playing!")
                    break
                else:
                    print("please enter Y or N")
            break
        else:
            if turn == 'X':
                 turn = 'O'
            else:
                turn = 'X'
            printBoard(theBoard)
