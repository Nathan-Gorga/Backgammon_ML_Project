import unittest
from game.board.board import Board  

class TestCanMove(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.whiteJail = 0
        self.board.blackJailJail = 0
        self.board.turn = "white"

    def test_valid_move_to_empty(self):
        self.board.board = [0]*24
        self.board.board[0] = 1  # white token
        self.assertTrue(self.board.canMove(0, 3, 1))  # move first file, by 3 moves and I am white

    def test_invalid_move_occupied_by_opponent(self):
        self.board.board = [0]*24
        self.board.board[0] = 1
        self.board.board[3] = -2  # 2 black tokens
        self.assertFalse(self.board.canMove(0, 3, 1))  # blocked

    def test_valid_move_on_single_opponent_token(self):
        self.board.board = [0]*24
        self.board.board[0] = 1
        self.board.board[3] = -1  # one black token
        self.assertTrue(self.board.canMove(0, 3, 1))  # allowed

    def test_cannot_move_if_token_in_jail(self):
        self.board.whiteJail = 1  # white token in jail
        self.board.blackJail = 0  # black token not in jail
        self.assertFalse(self.board.canMove(0, 3, 1))  # move forbidden

    def test_move_to_reserve_denied_if_not_all_in_camp(self):
        self.board.board = [1]*24  # white tokens not all in camp
        self.assertFalse(self.board.canMove(20, 5, 1))  # overshoot → reserve not allowed

    def test_move_to_reserve_allowed_if_all_in_camp(self):
        self.board.turn = "white"
        self.board.board = [0]*24
        # All white tokens in camp
        self.board.board[0:6] = [3,3,3,2,2,2]  # total = 15
        self.assertTrue(self.board.canMove(5, 6, 1))  # overshoot → reserve allowed

if __name__ == "__main__":
    unittest.main()

