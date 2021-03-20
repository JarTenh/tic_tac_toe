from time import sleep
from random import randint

def pick_starter(player, heads_or_tails, num_of_players):
    '''
    Contains the functionality to pick the starting player.
    '''

    rand_int = randint(1, 2)
    
    print('\nTossing the coin...')
    sleep(0.8)
    print('Coin is landing...')
    sleep(0.8)

    if rand_int == 1:
        print('It\'s HEADS!\n')
    else:
        print('It\'s TAILS!\n')
    sleep(0.5)
    if heads_or_tails == rand_int:
        print(f'Player {player}, you win! You start the game!')
    elif num_of_players == 1:
        print(f'Player {player}, you lose, computer starts.')
        player = 2
    else:
        print(f'Player {player}, you lose, ' \
        f'player {1 if player == 2 else 2} starts.')
        if player == 1:
            player = 2
        else:
            player = 1
    sleep(1.5)

    return player