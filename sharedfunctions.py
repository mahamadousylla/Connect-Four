#Mahamadou Sylla

import connectfour


def new_board(Board):
    '''
    changes the format of the board from 6x7 to 7x6
    '''
    result = [[Board[j][i] for j in range(len(Board))] for i in range(len(Board[0]))]
    new_board = []
    for r in result:
       new_board.append(r)
    return new_board


def get_move():
    '''
    asks the user what column they would like to make theyre move
    '''

    valid_columns = ['1','2','3','4','5','6','7']

    while True:

        player_move = input('Enter DROP or POP followed by the column number to make a move: ') #takes users move

        player_move = player_move.split() #splits players move to become a list of strings
        if len(player_move) == 2 and (player_move[0].upper() == 'DROP' or\
            player_move[0].upper() == 'POP')\
            and player_move[1] in valid_columns: #if length of players move equals 2 and if the user entered in drop or pop regardless of upper or lower case, and if number entered is in valid_columns
            return player_move #return players move

        else:
            print('Invalid move') #otherwise print this message
            print() 



def print_board(gameboard):
    '''
    prints the gameboard in a special format and checks whether each item is a R, Y or '.' and does a specific action
    '''
    
    board_copy = new_board(gameboard) #calls new_board function on given parameter and stores it in a variable called size
    size = len(board_copy[0]) #takes length of size
    for num in range(size): #for number in range in size
        print(num+1, end=' ') #prints each number + 1. increments 1 to account for indexing
    print('\n') # print new line after all numbers in range of size is done being printing
    for sub_list in board_copy: #for each sublist in the big list called board_copy
        for item in sub_list: #for item in sublist
            if item == 0: #if item is 0
                print('.', end= ' ') #print '.' 
            elif item == 1: #else if item is 1
                print('R', end = ' ') #print 'R'
            elif item == 2: #else if item is 2
                print('Y', end = ' ') #print 'Y'
                
        print('\n') #print a new line after every sublist
