import random

def dice():
    diceMin = 1
    diceMax = 6
    return random.randint(diceMin, diceMax)

def isDouble(roll1, roll2):

    return roll1 == roll2