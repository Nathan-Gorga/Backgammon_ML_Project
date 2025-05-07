from game.dice.dice import dice, isDouble


def startTurn():
    
    white = black = 0
    
    while white == black:
        white = dice() + dice()
        black = dice() + dice()
        
    return "white" if white > black else "black"


def isFileEmpty(token):
    return True if token == 0 else False

def isPlayerColor(token, colorPlayer):
    
    return (token > 0 and colorPlayer > 0) or (token < 0 and colorPlayer < 0)


def rollDice():
    roll1=dice()
    roll2=dice()
    print(f"you rolled {roll1} and {roll2}")
    return [roll1,roll2]

def changeTurn(colorPlayer):
    return "white" if colorPlayer == "black" else "black"





def playTurn(board,colorPlayer): #true if win, false if no win
    numMoves = 2
    
    #what is the color of the player
    moveDirection = 1 if colorPlayer == "white" else -1
    
    #dice roll
    rolls=rollDice()
    
    roll1=rolls[0]
    roll2=rolls[1]
   
    if isDouble(roll1,roll2):
        numMoves = 4
        rolls.append(roll1,roll2)
        print("double")
   

        

    # select token
    for move in range(numMoves):
        
        print(f"move {move+1}")
        
        isInJail = board.areYouInJail(moveDirection)
        while True: 
            
            # are you in jail?
            if isInJail:
                canGetOut = board.canGetOutOfJail(moveDirection, roll1, roll2)
                
                if canGetOut:
                    board.moveOutOfJail(canGetOut,moveDirection)
                
                
            else:  # not in jail
                
                boardIndex = int(input("which token are you moving? : ")) - 1
                token = board.board[boardIndex]
                diceRollThisMove = rolls[move]#TODO change so that you can choose to move the same token by roll1 or roll2 distance
                    
                #is there a token?
                if isFileEmpty(token):
                    print("ERROR : THERE ARE NO TOKENS ON THIS FILE")
                    continue
                #is the selected token of your color?
                if not isPlayerColor(token,moveDirection):
                    print("ERROR : THE SELECTED TOKEN IS NOT OF YOUR COLOR")
                    continue
                
                #can your token move there
                if not board.canMove(boardIndex,diceRollThisMove,moveDirection): # unit tested : OK
                    continue
                
                #move
                board.move(boardIndex,diceRollThisMove,moveDirection) # unit tested : OK
                
                
                break
        
    
        win = board.isItWin()
        if win:
            print(f"{colorPlayer} has won!")
            return True
        
    
    # change turn
    board.turn = changeTurn(colorPlayer)
    return False