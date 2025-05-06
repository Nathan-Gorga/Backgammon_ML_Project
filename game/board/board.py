from game.play_func.play_func import startTurn, isPlayerColor


BOARDSIZE = 24
NUM_TOKENS = 15



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
        self.blackJail = 0
        self.whiteJail = 0
        self.turn = startTurn()
        
    def printBoardInCLI(self):
        print(f"""
              
              it is {self.turn}'s turn to play
              
              black jail / white jail : {self.blackJail}/{self.whiteJail}
              
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
        
        
    def canGoInReserve(self):
        
        indexes = [0, 1, 2, 3, 4, 5] if self.turn == "white" else [23, 22, 21, 20, 19, 18]
        
        total = sum(self.board[i] for i in indexes)
        
        return abs(total) == NUM_TOKENS
        
    
    def areYouInJail(self, colorIndex):
        
        if colorIndex == 1: # white
            return not self.whiteJail == 0 
        else: #black
            return not self.blackJail == 0   
        
    def canMove(self,boardIndex, moveNumber, colorIndex):
        
        inReserve = False
        
        
        #is one of your guys in jail? (should not encouter this later as a function will handle it, just for now)
        if self.areYouInJail(colorIndex):
            print("ERROR : ONE OF YOUR TOKENS IS IN JAIL, YOU HAVE TO PLACE IT FIRST")
            return False
        
        #is it already occupied? 2 or more by other player
        moveAmount = moveNumber*colorIndex
        newIndex = boardIndex + moveAmount
        
        if newIndex >= 0:
            try:
                token = self.board[newIndex]
                if not (isPlayerColor(token,colorIndex) or abs(token) < 2):
                    print("ERROR : YOU CANNOT GO THERE, YOUR OPPONENT OCCUPIES THIS SPOT")
                    
                    return False
            except IndexError:
                inReserve = True
            
        else:
            inReserve = True
        
        #are you trying to get in the reserve and not everyone is here?
        if inReserve:
            reserveFull = self.canGoInReserve()
            if not reserveFull: # yes I know... for clarity with the return below
                print("ERROR : YOU CANNOT MOVE TO RESERVE, NOT ALL OF YOUR TOKENS ARE IN YOUR CAMP")
                return False

            
        #else True
        return True
    
    def move(self,boardIndex,moveNumber, colorIndex):
        
        
        toAdd = colorIndex*-1 # to decrement the absolute value of the token
        
        
        
        #is it crush: yes
        
        
        
        #is it crush : no



    