
from game.board.board import Board
from game.play_func.play_func import playTurn


if __name__ == "__main__":
    board = Board()
    board.printBoardInCLI()
    playTurn(board, board.turn)