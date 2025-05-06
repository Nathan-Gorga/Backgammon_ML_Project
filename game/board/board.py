BOARDSIZE = 24
# 0 : empty, 0 < : white, 0 > : black
STARTING_POSITION = [2,0,0,0,0,-5, # first pannel
                     0,-3,0,0,0,5, # second pannel
                     -5,0,0,0,3,0, # third pannel
                     5,0,0,0,0,-2] # fourth pannel


class Board:
    def __init__(self):
        self.size = BOARDSIZE
        self.board = STARTING_POSITION
        self.blackReserve = 0
        self.whiteReserve = 0
        self.jail = 0
        
    def printBoardInCLI(self):
        print(f"""
              jail : {self.jail}
              
              black reserve : {self.blackReserve}/{self.size}
              white reserve : {self.whiteReserve}/{self.size}""")
        
        half = self.size // 2
        
        firstHalf = self.board[:half][::-1]
        secondHalf = self.board[:half-1:-1]
        
        print(f"""
              BOARD :
              
              {secondHalf}
              {firstHalf}
              """)
        