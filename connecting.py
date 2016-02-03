#Mahamadou Sylla 61549479 and Jonathan Abebe 38104225


from collections import namedtuple
import socket

Connection_info = namedtuple('Connection_info', ['socket', 'input', 'output'])

        
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

