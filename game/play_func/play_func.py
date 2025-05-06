from ..dice.dice import dice, isDouble


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

    
def playTurn(board,colorPlayer):
    numMoves = 2
    
    #what is the color of the player
    moveDirection = 1 if colorPlayer == "white" else -1
    
    #dice roll
    rolls=rollDice()
    
    roll1=rolls[0]
    roll2=rolls[1]
   
    if isDouble(roll1,roll2):
        numMoves = 4
        print("double")
    #select token
    
    for moves in range(numMoves):
        print(f"move {moves+1}")
        while True: 
            boardIndex = int(input("which token are you moving? : ")) - 1
            token = board.board[boardIndex]
            if isFileEmpty(token):
                print("ERROR : THERE ARE NO TOKENS ON THIS FILE")
                continue
            if not isPlayerColor(token,moveDirection):
                print("ERROR : THE SELECTED TOKEN IS NOT OF YOUR COLOR")
                continue
            break
        
    
    #can move?
    
    #move
    
    #consequence
    
    #change turn
    