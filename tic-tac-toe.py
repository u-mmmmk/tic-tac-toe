#!/bin/python3

#unoptimized implementation of minimax to never lose at tic tac toe

#translate player moves to spots on the board
dict = {"a1":0, "a2":1, "a3":2, "b1":3, "b2":4, "b3":5, "c1":6, "c2":7, "c3":8}
''' 
spots on board and corresponding index in the array
[0] [1] [2] a
[3] [4] [5] b
[6] [7] [8] c
 1   2   3
'''

#main function
def main():
    global cpu #if computer is x or o
    global player #if the player is x or o
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "] #board
    print("tic tac toe!")
    player = input("Type 'X' to be X, or 'O' to be O. X will go first.\n").upper()
    if player == 'X':
        print("You are X.")
        cpu = 'O' #computer moves as o
        printboard(board)
        playermove(board)
    elif player == 'O':
        print("You are O.")
        cpu = 'X' #computer moves as x
    else:
        print("Invalid Character. \nComputer will move first.")
    tie = False
    won = False
    while won == False and tie == False:
        printboard(board)
        compmove(board)
        tie = checktie(board) #check if its a tie or win after every move
        won = checkwin(board)
        if won != False or tie != False:
            break
        printboard(board)
        playermove(board)
        tie = checktie(board)
        won = checkwin(board)
    printboard(board)
    if tie == True:
        print("Tie. No winner.")
    else:
        print(won, " won the game")

#print the board
def printboard(board):
    print('''
    [%s] [%s] [%s] a
    [%s] [%s] [%s] b
    [%s] [%s] [%s] c
     1   2   3
    '''%(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))
#is there a better way to do this? ^^^

#check if someone has won
def checkwin(board):
    '''
    horizontal increments by 1
    left diagonal increments by 2
    vertical increments by 3
    right diagonal increments by 4
    '''
    #check horizontal
    for i in 0,3,6: #only go through the top row of the board
         if board[i] != " " and board[i] == board[i + 1] == board[i + 2]:
                return board[i]
    #check vertical
    for i in 0,1,2:
        if board[i] != " " and board[i] == board[i + 3] == board[i + 6]:
            return board[i]
    #check right diagonal
    if board[0] != " " and board[0] == board[4] ==  board[8]:
        return board[0]
    #check left diagonal
    if board[2] != " " and board[2] == board[4] == board[6]:
        return board[2]
    return False

#check if it is a tie
def checktie(board):
    count = 0
    for i in board:
        if i == " ":
            return False
        else:
            count = count + 1
            if count == 9: #if the whole board is full then return True
                return True
    return False

#check if the spot is empty
def checkspace(move, board):
    if move not in dict:
        return False
    if board[dict[move]] == " ":
        return True
    else:
        return False

#input player move
def playermove(board):
    print("Your Move. Enter a square <row><column> ex: 'c2'")
    move = input().lower()
    if checkspace(move, board) == True:
        board[dict[move]] = player
    else:
        print("invalid move")
        playermove(board)
    return board


#input computers move
def compmove(board):
    print("Computer's move")
    bestscore = -9999 #initalize best score as a small number
    for i in range(9):
        if board[i] == " ":
            board[i] = cpu
            score = minimax(board, False)#call minimax with the current board and False because minimax is finding the best move for the player
            board[i] = " "
            if score > bestscore:
                bestscore = score
                move = i
    board[move] = cpu
    return


def minimax(position, maximize): #a variable called depth can also be included: define how many moves ahead minimax will look
    if checkwin(position) == cpu:
        return 1
    elif checkwin(position) == player:
        return -1
    elif checktie(position) == True:
        return 0
    if maximize == True: #find max score
        maxscore = -9999
        for i in range(9):
            if position[i] == " ":
                position[i] = cpu
                score = minimax(position, False)
                position[i] = " "
                maxscore = max(score, maxscore) #set maxscore to the greater score
        return maxscore
    else: #find min score
        minscore = 9999
        for i in range(9):
            if position[i] == " ":
                position[i] = player
                score = minimax(position, True)
                position[i] = " " 
                minscore = min(score, minscore) #set minscore to the smaller score
        return minscore

#call main
if __name__ == '__main__':
    main()