#Mahamadou Sylla 61549479 and Jonathan Abebe 38104225

# This module asks the user for information
#Problems:
'''Doesnt return the username from the namedtuple
Prints way too many things when running the actual code
'''
from collections import namedtuple
import socket
Game_info = namedtuple('Connect_information', ['name','move','turn'])
Connection_info = namedtuple('Connection_info', ['socket', 'input', 'output'])
User_info = namedtuple('User_info', ['username','host','port'])

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
        username = input('Username: ').strip()

        if len(username) > 0:
            return username
        else:
            print('That username is blank; please try again')



def _get_host()-> str:
    '''Gets the host from the user
    '''
    while True:
        host = input('Enter a host: ')

        if len(host) > 0:
            return host
        else:
            print('Enter a real host')
            
def _get_port()->str:
    '''Gets the port to connect to
    '''
    while True:
        port = int(input('Enter a port: '))
        if port < 0 or port > 65535 :
            print('Enter a real port between 0 and 65535')
        else:
            return port
            

def _whats_up()->None:
    print('Welcome to the connect4 game\n')


