#Mahamadou Sylla 61549479 and Jonathan Abebe 38104225

#Project #2 is on woodhouse.ics.uci.edu on port 4444

"""
1. Ask the user to specify a host, along the port
2. Ask the user for a username (shouldn't have whitespaces)
3. Connect to the server, if unsuccessful print an error specifying
the reason, if successful the game proceeds, Client is red

"""
from collections import namedtuple
import socket
import userinterface
import project2
import connectfour

Game_info = namedtuple('Connect_information', ['name','move','turn'])
Connection_info = namedtuple('Connection_info', ['socket', 'input', 'output'])
User_info = namedtuple('User_info', ['username', 'host','port'])
game = connectfour.new_game()

def random()->None:
    '''
    Calls the USerint module and returns the nametuple
    '''
    connection_tuple = userinterface._run_user_interface() #calls function for another module
    return connection_tuple #returns this 3 named namedtuple: username, host, port
    

    
def connection(host: str, port: int)-> Connection_info:
    '''
    Connects to the given host and port
    '''

    print('Connecting to Connect 4 server...')

    connect_socket = socket.socket() #connects to a socket

    connect_socket.connect((host, port)) #connects to the given host and port

    connect_input = connect_socket.makefile('r') #creates a way to easily read input from a server
    connect_output = connect_socket.makefile('w') #creates a way to easily send messaged to a server

    return Connection_info(socket = connect_socket,
                           input = connect_input,
                           output = connect_output) #returns this 3 field namedtuple: socket, input, output



_SHOW_DEBUG_TRACE = False


def send_move(connection: Connection_info, message:str)-> None:
    '''
    takes in a connection that is assumed to have been made
    and sends a message to the server
    '''
    
    connection.output.write(message + '\r\n') #sends a message to a server and includes the end of line character
    connection.output.flush() #sends message immediately

    if _SHOW_DEBUG_TRACE: #if this evaluates to True (this can be found above this function
        print('SENT: ' + message) #prints the message that was sent to the server

def read_line(connection: Connection_info) -> str:
    '''
    takes in a connection that is assumed to have been made
    and reads a message the server sent back
    '''

    # The [:-1] uses the slice notation to remove the last character
    # from the string.  Since we know that readline() will always
    # return a line of text with a '\n' character on the end of it,
    # the slicing here will ensure that these will always be stripped
    # out, so we'll never have to deal with this detail elsewhere.

    message = connection.input.readline()[:-1] #saves message read from server and excludes the new line character

    if _SHOW_DEBUG_TRACE: #if this evaluates to True (this can be found above this function)

        print('RCVD: ' + message) #prints the message that was sent to the server

    return message #return the message sent


def close(connection: 'connection') -> None:
    '''
    Closes a connection
    '''
   
    # Closing a connection requires closing the pseudo-file objects and
    # then closing the socket, so we'll do all of that here.
    connection.input.close() #closes input connection
    connection.output.close() #closes output connection
    connection.socket.close() #closes socket connection


def main_program(game):
    '''
    program that handles the connect four game
    '''
    try:
        
        x = random() #(prompts user for a username, host and port. this is the first function in this module
        c = connection(x.host, x.port) #connects to given host and port
        send_move(c, 'I32CFSP_HELLO ' + x.username) #send a message and includes the username provided by user
        read_line(c) #reads a line from the server
        send_move(c, 'AI_GAME') #sends this message to the server
        read_line(c) #reads a line from the server
        
        while connectfour.winner(game) == 0: #while there is no winner

            if game.turn == 1: #if it is player 
                print('Player RED make your move') #prints this message
                print()


                project2.print_board(game.board) #print a new game


                while True:

                    try:
                        current_move = project2.get_move() #gets the players move and stores it in a variable
                        print('\n')
                        
                        if current_move[0].upper().startswith('DROP'): #takes players input at first index, makes it uppercase and checks if it equals a string
                            current_move = int(current_move[-1]) #converts players move at last index to an integer
                            current_move = current_move - 1 #subtracts 1 from players move to account for indexing
                            game = connectfour.drop(game, current_move) #calls drop function from connectfour module that handles dropping a piece onto connect four board
                            project2.print_board(game.board) #prints updated game board
                            send_move(c, 'DROP ' + str(current_move+1)) #sends string and adds one to players move to account for subtractoin earlier then converts players move back to a string to send to the server
                            break #leaves the function
              


                        elif current_move[0].upper().startswith('POP'): #takes players input at first index, makes it uppercase and checks if it equals a string
                            current_move = int(current_move[-1]) #converts players move at last index to an integer
                            current_move = current_move - 1 #subtracts 1 from players move to account for indexing
                            game = connectfour.pop(game, current_move) #calls pop function from connectfour module that handles popping a piece onto connect four board
                            project2.print_board(game.board) #prints updated game board
                            send_move(c, 'POP ' + str(current_move+1)) #sends string and adds one to players move to account for subtractoin earlier then converts players move back to a string to send to the server
                            break #leaves the function

                    except:
                        print('Invalid Move') #prints this message if try statement fails
                        print()
            
                    
                
            elif game.turn == 2: #if it is the servers move

                read_line(c) #read input from server
                servers_move = read_line(c) #reads another line from server. this is servers move

                if servers_move.startswith('POP'): #if servers move starts with POP
                    servers_move = int(servers_move.split()[-1]) #split servers input and grab last index and convert to an integer
                    servers_move = servers_move - 1 #subtracts one from servers move to account for 0 indexing
                    read_line(c) #read line of input from server
                    game = connectfour.pop(game, servers_move) #calls pop function from connectfour module that handles popping a piece onto connect four board
                    project2.print_board(game.board) #prints updated game board

                else:
                    servers_move = int(servers_move.split()[-1]) #split servers input and grab last index and convert to an integer
                    servers_move = servers_move - 1 #subtracts one from servers move to account for 0 indexing
                    read_line(c) #read line of input from server
                    game = connectfour.drop(game, servers_move) #calls drop function from connectfour module that handles dropping a piece onto connect four board
                    project2.print_board(game.board) #prints updated game board


            print('\n\n')
        project2.print_board(game.board) #prints new game state
        print('Game Over') #when the game is over prints this message
        if game.turn == 1: #if it is red players turn (player red has lost)
            print('Sorry, you have lost') #prints this message
        elif game.turn == 2: #if it yellow players move (player yellow has lost)
            print('Congratulations! You have won') #prints this message

    finally:
        
        close(c) #closes the connection


if __name__ == '__main__':
    main_program(game)
    

### invalid username, port, host
