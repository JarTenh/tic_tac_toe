import sys

from modules.ui import intro, how_many_players, play_game, \
    who_starts, show_instructions, play_again
from modules.clear_screen import clear


def launch_game():
    while True:
        intro()
        num_players = how_many_players()
        starter = who_starts(num_players)
        show_instructions()
        play_game(starter, num_players)
        if not play_again():
            break
    return

if __name__ == '__main__':
    clear()
    launch_game()
    clear()
    print('See you soon!')
    print()
    sys.exit()
