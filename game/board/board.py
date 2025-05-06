from ..play_func.play_func import startTurn


BOARDSIZE = 24
# 0 : empty, 0 < : white, 0 > : black
STARTING_POSITION = [2,0,0,0,0,-5, # first pannel
                     0,-3,0,0,0,5, # second pannel
                     -5,0,0,0,3,0, # third pannel
                     5,0,0,0,0,-2] # fourth pannel


FIRST_HALF_INDEX = [12,11,10,9,8,7,6,5,4,3,2,1]
SECOND_HALF_INDEX = [13,14,15,16,17,18,19,20,21,22,23,24]

class Board:
    def __init__(self):
        self.size = BOARDSIZE
        self.board = STARTING_POSITION
        self.blackReserve = 0
        self.whiteReserve = 0
        self.jail = 0
        self.turn = startTurn()
        
    def printBoardInCLI(self):
        print(f"""
              
              it is {self.turn}'s turn to play
              
              jail : {self.jail}
              
              black reserve : {self.blackReserve}/{self.size}
              white reserve : {self.whiteReserve}/{self.size}""")
        
        half = self.size // 2
        
        firstHalf = self.board[:half][::-1]
        secondHalf = self.board[:half-1:-1]
        
        print(f"""
              BOARD :
              {SECOND_HALF_INDEX}
              {secondHalf}
              {firstHalf}
              {FIRST_HALF_INDEX}
              """)
        