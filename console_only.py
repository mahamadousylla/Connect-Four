#Mahamadou Sylla

import connectfour
import sharedfunctions

game = connectfour.new_game() #brand new game of connect four


def program(game):
    '''
    program that handles the connect four game
    '''
    while connectfour.winner(game) == 0: #while there is no winner
        if game.turn == 1: #if it is red player's turn
            print('Player RED make your move') #prints this message
            print()
        elif game.turn == 2: #if it is yellow players turn
            print('Player YELLOW make your move') #prints this message
            print()
        sharedfunctions.print_board(game.board) #print a new game
        current_move = sharedfunctions.get_move() #gets the players move and stores it in a variable
        
        while True:

            try:

                if current_move[0].upper() == 'DROP': #if players says they want to drop
                    game = connectfour.drop(game, int(current_move[-1])-1) #drops the players move in appropriate column and changes the game state
                elif current_move[0].upper() == 'POP': #if player says they want to pop
                    game = connectfour.pop(game, int(current_move[-1])-1) #pops players move as long as players piece is in specified column

            except:
                print('Invalid Move') #if playes move is invalid prints this message
                print()
                current_move = sharedfunctions.get_move() #recursively ask for players move until input is acceptable
            else:
                break #leave the function
        print('\n\n')
    sharedfunctions.print_board(game.board) #prints new game state
    print('Game Over') #when game is over prints this message
    if game.turn == 1: #if it is red playes turn
        print('Player YELLOW is the Winner') #print this message
    elif game.turn == 2: #if is is yellow players turn
        print('Player RED is the Winner') #print this message
        
if __name__ == '__main__':
    program(game)
