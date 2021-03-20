class Game():
    '''
    Contains the game class, from where one can create
    a tic-tac-toe game. 
    '''

    def __init__(self, turn, ai = False) -> None:
        self.turn = turn
        self.board = [' '] * 9
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.ai = ai

    def __repr__(self) -> str:
        return 'Contains the game class, from where one can create ' \
                'a tic-tac-toe game.'
    
    def __str__(self) -> str:
        return 'Contains the game class, from where one can create ' \
                'a tic-tac-toe game.'

    def print_board(self):
        '''
        Print the board using "print" statement
        '''

        print(f'Player 1: {self.player_1}')
        if self.ai:
            print('Computer: O')
        else:
            print(f'Player 2: {self.player_2}')
        print()
        print(f'''
          --- --- ---
         | {self.board[0]} | {self.board[1]} | {self.board[2]} |
          --- --- ---
         | {self.board[3]} | {self.board[4]} | {self.board[5]} |
          --- --- ---
         | {self.board[6]} | {self.board[7]} | {self.board[8]} |
          --- --- ---
        ''')

    def change_turn(self):
        '''
        Switch turns.
        '''
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def place_marker(self, grid_number):
        '''
        Place the marker on the board. If the spot is already taken
        return -1. Otherwise return 0.
        '''

        marker = ''

        if self.turn == 1:
            marker = self.player_1
        else:
            marker = self.player_2
        
        if self.board[grid_number - 1] == ' ':
            self.board[grid_number - 1] = marker
            return 0
        else:
            return -1

    def has_winner(self):
        '''
        Checks if there is three same symbols in a row on the board.
        If it exists, the winner is found.
        '''

        if ((self.board[0] == self.board[1] == self.board[2]) and \
            ((self.board[0] != ' ') or (self.board[1] != ' ') or (self.board[2] != ' '))) or \
            ((self.board[3] == self.board[4] == self.board[5]) and \
            ((self.board[3] != ' ') or (self.board[4] != ' ') or (self.board[5] != ' '))) or \
            ((self.board[6] == self.board[7] == self.board[8]) and \
            ((self.board[6] != ' ') or (self.board[7] != ' ') or (self.board[8] != ' '))) or \
            ((self.board[0] == self.board[4] == self.board[8]) and \
            ((self.board[0] != ' ') or (self.board[4] != ' ') or (self.board[8] != ' '))) or \
            ((self.board[2] == self.board[4] == self.board[6]) and \
            ((self.board[2] != ' ') or (self.board[4] != ' ') or (self.board[6] != ' '))) or \
            ((self.board[0] == self.board[3] == self.board[6]) and \
            ((self.board[0] != ' ') or (self.board[3] != ' ') or (self.board[6] != ' '))) or \
            ((self.board[1] == self.board[4] == self.board[7]) and \
            ((self.board[1] != ' ') or (self.board[4] != ' ') or (self.board[7] != ' '))) or \
            ((self.board[2] == self.board[5] == self.board[8]) and \
            ((self.board[2] != ' ') or (self.board[5] != ' ') or (self.board[8] != ' '))):
            return True
        
        return False

    def open_grids_available(self):
        '''
        Check if there is at least one free grid left on the board.
        '''

        if ' ' in self.board:
            return True
        return False

    def winner(self, ai = False):
        self.print_board()
        print()
        if ai:
            print('COMPUTER WINS! You lose!')
        else:
            print(f'CONGRATULATIONS player {self.turn}! You WIN the game!')
        print()

    def tie(self):
        self.print_board()
        print()
        print('Looks like the result is a tie!')
        print()
