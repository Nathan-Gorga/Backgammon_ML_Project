import unittest
from game.board.board import Board


class TestIsItCrush(unittest.TestCase):
    def setUp(self):
        from board.board import Board  # ajuste si le chemin est différent
        self.board = Board()

    def test_white_lands_on_black(self):
        self.board.board[3] = -1  # noir
        result = self.board.isItCrush(3, 1)  # blanc arrive
        self.assertTrue(result)

    def test_black_lands_on_white(self):
        self.board.board[4] = 1  # blanc
        result = self.board.isItCrush(4, -1)  # noir arrive
        self.assertTrue(result)

    def test_white_lands_on_white(self):
        self.board.board[5] = 1  # blanc
        result = self.board.isItCrush(5, 1)  # blanc arrive
        self.assertFalse(result)

    def test_black_lands_on_black(self):
        self.board.board[6] = -1  # noir
        result = self.board.isItCrush(6, -1)  # noir arrive
        self.assertFalse(result)

    def test_white_lands_on_empty(self):
        self.board.board[7] = 0
        result = self.board.isItCrush(7, 1)
        self.assertFalse(result)

    def test_black_lands_on_empty(self):
        self.board.board[8] = 0
        result = self.board.isItCrush(8, -1)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
