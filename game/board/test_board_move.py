import unittest
from game.board.board import Board

class TestMoveFunction(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.board = [0]*24  # Empty board for clean setup
        self.board.whiteJail = 0
        self.board.blackJail = 0

    def test_simple_white_move(self):
        self.board.board[0] = 1  # 1 white token
        self.board.move(0, 3, 1)  # Move 3 spaces
        self.assertEqual(self.board.board[3], 1)  # Should be at index 3
        self.assertEqual(self.board.board[0], 0)  # Removed from index 0

    def test_simple_black_move(self):
        self.board.board[5] = -1  # 1 black token
        self.board.move(5, 2, -1)  # Move 2 spaces backwards
        self.assertEqual(self.board.board[3], -1)
        self.assertEqual(self.board.board[5], 0)

    def test_crush_white_hits_black(self):
        self.board.board[0] = 1  # white token
        self.board.board[3] = -1  # black token to crush
        self.board.move(0, 3, 1)
        self.assertEqual(self.board.blackJail, 1)
        self.assertEqual(self.board.board[3], 1)

    def test_crush_black_hits_white(self):
        
        
        blacktokenindex = 5
        whitetokenindex = 0
        tomove = abs(blacktokenindex-whitetokenindex)

        # Put a single white token where black will land
        self.board.board[whitetokenindex] = 1  # white token
        self.board.board[blacktokenindex] = -1  # black token about to move
        self.board.move(blacktokenindex, tomove, -1)  # black moves 5 steps
        
        self.assertEqual(self.board.whiteJail, 1)
        self.assertEqual(self.board.board[whitetokenindex], -1)  # black replaces white
        self.assertEqual(self.board.board[blacktokenindex], 0)   # original place now empty

    def test_move_to_reserve_white(self):
        self.board.board[23] = 1  # white token near end
        self.board.whiteReserve = 0
        self.board.move(23, 1, 1)  # Move past last index
        self.assertEqual(self.board.whiteReserve, 1)

    def test_move_to_reserve_black(self):
        self.board.board[0] = -1  # black token near start
        self.board.blackReserve = 0
        self.board.move(0, 1, -1)  # Move to -1 (past start)
        self.assertEqual(self.board.blackReserve, 1)

if __name__ == '__main__':
    unittest.main()
