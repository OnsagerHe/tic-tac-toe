import unittest
from io import StringIO
import sys
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    
    def setUp(self):
        """ Set up a fresh TicTacToe game before every test """
        self.game = TicTacToe()
        self.game.create_board()

    def test_create_board(self):
        """ Test if the board is created correctly """
        self.assertEqual(self.game.board, [['-' for _ in range(3)] for _ in range(3)])
    
    def test_fix_spot(self):
        """ Test if a player can mark a spot correctly """
        self.game.fix_spot(0, 0, 'X')
        self.assertEqual(self.game.board[0][0], 'X')

    def test_swap_player_turn(self):
        """ Test player swap logic """
        self.assertEqual(self.game.swap_player_turn('X'), 'O')
        self.assertEqual(self.game.swap_player_turn('O'), 'X')
    
    def test_is_board_filled(self):
        """ Test if the game correctly detects a filled board """
    # TODO: If the board is full, check that the function returns True and vice versa.

    def test_is_player_win_row(self):
        """ Test if the game correctly detects a row win """
        # TODO: In a configuration where player “X” has a row,
        # check that the is_player_win function returns True for “X” and
        # False for “O” and vice versa.

    def test_is_player_win_column(self):
        """ Test if the game correctly detects a column win """
        # TODO: In a configuration where player “X” has a column,
        # check that the is_player_win function returns True for “X” and
        # False for “O” and vice versa.

    def test_is_player_win_diagonal(self):
        """ Test if the game correctly detects a diagonal win """
        # TODO: In a configuration where player “X” has a diagonal,
        # check that the is_player_win function returns True for “X” and
        # False for “O” and vice versa.


    def test_display_board(self):
        """ Test the display_board output """
        expected_output = "- - -\n- - -\n- - -\n\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        self.game.display_board()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()