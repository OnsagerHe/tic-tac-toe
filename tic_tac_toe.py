import random

# Documentation class: https://docs.python.org/3/tutorial/classes.html
class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def get_random_first_player(self):
        # TODO: this value is set to 0. Can you return 0 or 1 at random?
        return 0

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        # TODO: check rows columns with 3 identical value

        # TODO: check columns columns with 3 identical value

        # TODO: check diagonals columns with 3 identical value
        return False

    def is_board_filled(self):
        # TODO: check that all board values are taken
        return False

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player}'s turn")
            self.display_board()

            # Get user input
            # TODO: try - except enter two numbers between 1 and 3
            # Documentation: https://docs.python.org/3/tutorial/errors.html#handling-exceptions
            row, col = map(int, input("Enter row and column numbers to fix spot (1-3): ").split())
            # TODO: Check if spot are already taken
            
            self.fix_spot(row - 1, col - 1, player)

            # Check if the current player has won
            # TODO: call function is_player_win

            # Check if the game is a draw
            # TODO: call function is_board_filled

            # Swap turn
            player = self.swap_player_turn(player)

        # Display the board result
        self.display_board()