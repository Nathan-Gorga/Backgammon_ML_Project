from game.play_func.play_func import startTurn, isPlayerColor, isFileEmpty


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
    
    
    def indexHitsInReserve(self, index):
        
        if index < 0:
            return True
        
        if index >= BOARDSIZE:
            return True

        return False
               

        
    def canGoInReserve(self):
        
        indexes = [0, 1, 2, 3, 4, 5] if self.turn == "white" else [23, 22, 21, 20, 19, 18]
        
        total = sum(self.board[i] for i in indexes)
        
        return abs(total) == NUM_TOKENS
        
    
    def areYouInJail(self, colorIndex):
        
        if colorIndex == 1: # white
            return not self.whiteJail == 0 
        else: #black
            return not self.blackJail == 0   
                
        
    def isItCrush(self, index, colorIndex):
        whereTokenIsGoing = self.board[index]

        if colorIndex > 0:  #white
            return whereTokenIsGoing == -1
        else:  # black
            return whereTokenIsGoing == 1
        
    def crush(self,destination, colorPlayer): #
        
        
        if colorPlayer == 1: #white
            self.blackJail += 1    
        else: #black
            self.whiteJail += 1
        
        self.board[destination] = 0 
        self.board[destination] += colorPlayer 
    
    
    def isItFriendlyFile(self,destination, colorPlayer): 
        
        return isFileEmpty(self.board[destination - 1]) or isPlayerColor(self.board[destination-1],colorPlayer) 
    
    
    
    def canMove(self,boardIndex, moveNumber, colorIndex):
        

        
        
        #is one of your guys in jail? (should not encouter this later as a function will handle it, just for now)
        if self.areYouInJail(colorIndex):
            print("ERROR : ONE OF YOUR TOKENS IS IN JAIL, YOU HAVE TO PLACE IT FIRST")
            return False
        
        #is it already occupied? 2 or more by other player
        moveAmount = moveNumber*colorIndex
        newIndex = boardIndex + moveAmount
        
        if not self.indexHitsInReserve(newIndex):
        
            token = self.board[newIndex]
            if not (isPlayerColor(token,colorIndex) or abs(token) < 2):
                print("ERROR : YOU CANNOT GO THERE, YOUR OPPONENT OCCUPIES THIS SPOT")
                
                return False
        
        else:
            #are you trying to get in the reserve and not everyone is here?
            reserveFull = self.canGoInReserve()
            if not reserveFull: # yes I know... for clarity with the return below
                print("ERROR : YOU CANNOT MOVE TO RESERVE, NOT ALL OF YOUR TOKENS ARE IN YOUR CAMP")
                return False
            
        #else True
        return True
    
    def move(self, boardIndex, moveNumber, colorIndex):        
        moveAmount = moveNumber * colorIndex
        newIndex = boardIndex + moveAmount

        # Enlève le pion de sa case d'origine
        self.board[boardIndex] -= colorIndex

        # Est-ce que le mouvement mène à la réserve ?
        if self.indexHitsInReserve(newIndex):
            if colorIndex > 0:
                self.whiteReserve += 1
                print(f"A WHITE TOKEN HAS ENTERED THE RESERVE | WHITE RESERVE : {self.whiteReserve}/{NUM_TOKENS}")
            else:
                self.blackReserve += 1
                print(f"A BLACK TOKEN HAS ENTERED THE RESERVE | BLACK RESERVE : {self.blackReserve}/{NUM_TOKENS}")
            return

        
        crush = self.isItCrush(newIndex, colorIndex)       

        if crush:
            self.crush(newIndex,colorIndex)  
        else:
            self.board[newIndex] += colorIndex

    def canGetOutOfJail(self,colorPlayer,roll1,roll2): # returns dice used if got out of jail, else returns False
        
        file1 = file2 = None
        boundMax = boundMin = 0
        if colorPlayer == 1: #white
           
            boundMax = 6
            boundMin = 1
           
            file1 = self.isItFriendlyFile(roll1-1,1) or self.isItCrush(roll1-1, 1)
            file2 = self.isItFriendlyFile(roll2-1,1) or self.isItCrush(roll2-1, 1)
            
        else: #black
            
            boundMax = 24
            boundMin = 19
            
            file1 = self.isItFriendlyFile(BOARDSIZE-roll1,-1) or self.isItCrush(BOARDSIZE - roll1, -1)
            file2 = self.isItFriendlyFile(BOARDSIZE-roll2,-1) or self.isItCrush(BOARDSIZE - roll2, -1)
        
        print(f"File {roll1} is {"empty" if file1 else "blocked"} and File {roll2} is {"empty" if file2 else "blocked"}")
        
        if file1 or file2:
        
            while True:               
                choice = input("which do you choose? : ")
        
                if isFileEmpty(self.board[choice-1]) and choice >= boundMin and choice <= boundMax:
                    break
        
                else:
                    print("ERROR : THIS FILE IS NOT EMPTY")
        
            return choice
        
        print("YOU ARE UNABLE TO GET OUT OF JAIL")
        return False
        
           
    def moveOutOfJail(self,choice,colorPlayer):
        
        #is it crush?
        isItCrush = self.isItCrush(choice,colorPlayer)
        if isItCrush:
            self.crush(choice-1,colorPlayer)        
        else: #add to file
            self.board[choice-1] += colorPlayer
        
        
           
    def isItWin(self):
        return self.whiteReserve == NUM_TOKENS or self.blackReserve ==  NUM_TOKENS
            
            

    