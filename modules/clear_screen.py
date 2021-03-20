'''
Module for clearing screen terminal. Works on Windows/Mac/Linux
'''

import os

def clear():
    '''
    Clears the terminal screen.
    '''

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')