'''
This module handles the interaction between user(s) and
the app. All the input from user(s) goes through here.
'''

from random import randint
import sys
from modules.pick_starting_player import pick_starter
from modules.game import Game
from modules.clear_screen import clear
from time import sleep

def intro():
    '''
    Prints the welcome text to tic-tac-toe.
    '''
    print()
    print('*******************************')
    print('    WELCOME TO TIC_TAC_TOE!')
    print('*******************************')
    print()
    print('(Press ctrl-c to quit the game)')
    print()


def how_many_players():
    '''
    Determines how many players play the game based on user input.
    '''
    num_of_players = 0

    while True:
        try:
            num_of_players = int(input(
                'How many players play the game (1 or 2)? '
                ))
            if (num_of_players > 0) and (num_of_players < 3):
                break
            else:
                raise ValueError
        except ValueError:
            print('Please provide a valid input (1 or 2 players)\n')
        except KeyboardInterrupt:
            print('\nSee you later!')
            sys.exit()
    
    return num_of_players


def who_starts(num_of_players):
    '''
    Determines who starts the game.
    '''
    # Default value for heads or tails picker.
    player = 1

    # In case there are two players, the heads or tails picker gets
    # choosed.
    if num_of_players == 2:
        player = randint(1, 2)

    print()
    print('Great!')
    print('Let\'s determine who starts the game!')
    print()

    while True:
        try:
            heads_or_tails = int(input(
                f'Player {player}, pick heads (1) or tails (2): '
                ))
            if (heads_or_tails > 0) and (heads_or_tails < 3):
                break
            else:
                raise ValueError
        except ValueError:
            print('Please provide a valid input!\n')
        except KeyboardInterrupt:
            print('\nSee you later!')
            sys.exit()
    
    return pick_starter(player, heads_or_tails, num_of_players)
    

def show_instructions():
    '''
    Shows the instructions of how to play the game.
    '''
    try:
        clear()
        print('GAME INSTRUCTIONS')
        print()
        print('Place your marker on the board ' \
            'by giving a number specified in the grid map.')
        print()
        print(' --- --- ---\n' \
            '| 1 | 2 | 3 |\n' \
            ' --- --- ---\n' \
            '| 4 | 5 | 6 |\n' \
            ' --- --- ---\n' \
            '| 7 | 8 | 9 |\n' \
            ' --- --- ---\n'
        )
        input('Press \'Enter\' to continue... ')

    except KeyboardInterrupt:
        print()
        print('See you soon!')
        sys.exit()
    
    return

def play_game(starter, num_players):
    '''
    Starts the game.
    '''

    game = Game(starter)

    if num_players == 1:
        game.ai = True
    
    while True:
        clear()
        game.print_board()
        print()

        # Computer's turn in one-player game
        if game.ai and game.turn == 2:
            print('it\'s computer\'s turn!')
            sleep(0.5)
            print('Thinking...')
            sleep(0.8)
            print('This is a brilliant move!')
            sleep(1)
            while True:
                if game.place_marker(randint(1, 9)) == 0:
                    if game.has_winner():
                        clear()
                        game.winner(ai = True)
                        return
                    if game.open_grids_available():
                        game.change_turn()
                    else:
                        clear()
                        game.tie()
                        return
                    break

        # Two player game and human's turn in one-player game
        else:
            print(f'It\'s player {game.turn}\'s turn!')
            print('Press "i + enter" to show game instructions')
            print()
            try:
                grid = input('Place your marker (grid number 1 - 9): ')
                if grid == 'i' or grid == 'I':
                    show_instructions()
                    continue
                grid = int(grid)
                if (grid > 0) and (grid < 10):
                    if game.place_marker(grid) == 0:
                        if game.has_winner():
                            clear()
                            game.winner()
                            return
                        if game.open_grids_available():
                            game.change_turn()
                        else:
                            clear()
                            game.tie()
                            return
                    else:
                        print('That grid is already taken!')
                        sleep(0.5)
                else:
                    raise ValueError
            except ValueError:
                print('Please provide a valid input!')
                sleep(0.5)
            except KeyboardInterrupt:
                print()
                print('See you soon!')
                sys.exit()

def play_again():
    '''
    Ask the user wether or not play the game again.
    '''
    while True:
        try:
            answer = input('Do you want to play again (y/n)? ')
            if answer in ['y', 'Y']:
                clear()
                return True
            elif answer in ['n', 'N']:
                return False
            else:
                raise ValueError
        except ValueError:
            print('Please provide a valid input!')
