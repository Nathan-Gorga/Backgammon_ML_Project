from ..dice.dice import dice


def startTurn():
    
    white = black = 0
    
    while white == black:
        white = dice() + dice()
        black = dice() + dice()
        
    return "white" if white > black else "black"
    
    