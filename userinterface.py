#Mahamadou Sylla 61549479 and Jonathan Abebe 38104225

from collections import namedtuple
import socket
import connecting
import connectfour
import sharedfunctions

game = connectfour.new_game()
Game_info = namedtuple('Connect_information', ['name','move','turn'])
Connection_info = namedtuple('Connection_info', ['socket', 'input', 'output'])
User_info = namedtuple('User_info', ['username','host','port'])

def random()->None:
    '''
    Calls the _run_user_interface() function and returns the nametuple
    '''
    connection_tuple = _run_user_interface() #calls function for another module
    return connection_tuple #returns this 3 named namedtuple: username, host, port


def main_program(game):
    '''
    program that handles the connect four game
    '''
    try:
        
        x = random() #(prompts user for a username, host and port. this is the first function in this module
        c = connecting.connection(x.host, x.port) #connects to given host and port
        connecting.send_move(c, 'I32CFSP_HELLO ' + x.username) #send a message and includes the username provided by user
        connecting.read_line(c) #reads a line from the server
        connecting.send_move(c, 'AI_GAME') #sends this message to the server
        connecting.read_line(c) #reads a line from the server
        
        while connectfour.winner(game) == 0: #while there is no winner

            if game.turn == 1: #if it is player 
                print('Player RED make your move') #prints this message
                print()


                sharedfunctions.print_board(game.board) #print a new game


                while True:

                    try:
                        current_move = sharedfunctions.get_move() #gets the players move and stores it in a variable
                        print('\n')
                        
                        if current_move[0].upper().startswith('DROP'): #takes players input at first index, makes it uppercase and checks if it equals a string
                            current_move = int(current_move[-1]) #converts players move at last index to an integer
                            current_move = current_move - 1 #subtracts 1 from players move to account for indexing
                            game = connectfour.drop(game, current_move) #calls drop function from connectfour module that handles dropping a piece onto connect four board
                            sharedfunctions.print_board(game.board) #prints updated game board
                            connecting.send_move(c, 'DROP ' + str(current_move+1)) #sends string and adds one to players move to account for subtractoin earlier then converts players move back to a string to send to the server
                            break #leaves the function
              


                        elif current_move[0].upper().startswith('POP'): #takes players input at first index, makes it uppercase and checks if it equals a string
                            current_move = int(current_move[-1]) #converts players move at last index to an integer
                            current_move = current_move - 1 #subtracts 1 from players move to account for indexing
                            game = connectfour.pop(game, current_move) #calls pop function from connectfour module that handles popping a piece onto connect four board
                            sharedfunctions.print_board(game.board) #prints updated game board
                            connecting.send_move(c, 'POP ' + str(current_move+1)) #sends string and adds one to players move to account for subtractoin earlier then converts players move back to a string to send to the server
                            break #leaves the function

                    except:
                        print('Invalid Move') #prints this message if try statement fails
                        print()
            
                    
                
            elif game.turn == 2: #if it is the servers move

                connecting.read_line(c) #read input from server
                servers_move = connecting.read_line(c) #reads another line from server. this is servers move

                if servers_move.startswith('POP'): #if servers move starts with POP
                    servers_move = int(servers_move.split()[-1]) #split servers input and grab last index and convert to an integer
                    servers_move = servers_move - 1 #subtracts one from servers move to account for 0 indexing
                    connecting.read_line(c) #read line of input from server
                    game = connectfour.pop(game, servers_move) #calls pop function from connectfour module that handles popping a piece onto connect four board
                    sharedfunctions.print_board(game.board) #prints updated game board

                else:
                    servers_move = int(servers_move.split()[-1]) #split servers input and grab last index and convert to an integer
                    servers_move = servers_move - 1 #subtracts one from servers move to account for 0 indexing
                    connecting.read_line(c) #read line of input from server
                    game = connectfour.drop(game, servers_move) #calls drop function from connectfour module that handles dropping a piece onto connect four board
                    sharedfunctions.print_board(game.board) #prints updated game board


            print('\n\n')
        sharedfunctions.print_board(game.board) #prints new game state
        print('Game Over') #when the game is over prints this message
        if game.turn == 1: #if it is red players turn (player red has lost)
            print('Sorry, you have lost') #prints this message
        elif game.turn == 2: #if it yellow players move (player yellow has lost)
            print('Congratulations! You have won') #prints this message
    except:
        print('The connection was unsuccessful')

    finally:

        try:
            connecting.close(c) #closes the connection

        except:
            print('Goodbye')




            
def _run_user_interface()->'Connection_info':
    '''Combination of everything
    '''
    _whats_up()
    username1 = _ask_for_username()

    host1 = _get_host()
    port1 = _get_port()
    
    return User_info(username = username1, host = host1, port = port1)


    


def _ask_for_username() -> str:
    '''
    Asks the user to enter a username and returns it as a string.  Continues
    asking repeatedly until the user enters a username that is non-empty, as
    the Polling server requires.
    '''
    while True:
        username = input('Please enter in your username: ').strip()

        if len(username) > 0 and ' ' not in username:
            return username
        else:
            print('That is not a valid username. Please enter a valid username')
            print()


def _get_host()-> str:
    '''Gets the host from the user
    '''
    while True:
        host = input('Enter the host you would like to connect to: ')

        if len(host) > 0:
            return host
        else:
            print('That is not a valid host. Please enter a real host')
            
def _get_port()->str:
    '''Gets the port to connect to
    '''
    while True:
        port = int(input('Enter the port you would like to connect to: '))
        if port < 0 or port > 65535:
            print('That is not a valid port. Please enter a real port between 0 and 65535')
    
        else:
            return port
            

def _whats_up()->None:
    print('Welcome to the Connect 4 game\n')



if __name__ == '__main__':
    main_program(game)
    
