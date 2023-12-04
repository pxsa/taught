import os
import numpy


map = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
turn = 0

def printMap():
    for i in map:
        print(i)

def anylis(userinput, turn):
    row = userinput // 3
    col = userinput % 3

    if isRepeated(row, col):
        return False
    


    element = "X" if turn % 2 == 0 else "O"
    map[row][col] = element
    return True
    

def isRepeated(row, col):
    return map[row][col] != "0"

def isFull():
    mapString = ""
    for row in map:
        mapString += ''.join(row)

    return '0' not in mapString   

def rowWinner(turn):
    element = "XXX" if turn % 2 == 0 else "OOO"
    
    for row in map:
        rowString = ''.join(row)
        if element == rowString:
            return True
    return False

def columnWin(turn):
    npmap = numpy.array(map).T
    element = "XXX" if turn % 2 == 0 else "OOO"
    
    for row in npmap:
        rowString = ''.join(row)
        if element == rowString:
            return True
    return False

def isWinner(turn):
    if rowWinner(turn) or columnWin(turn):
        return True
    return False

while True:
    os.system("clear")
    printMap()


    userInput = int(input("Enter a location (1-9): "))
    valid = anylis(userInput-1, turn)

    if isWinner(turn):
        os.system("clear")
        printMap()
        player = "Player 1" if turn % 2 == 0 else "Player2"
        print(f"{player} wins the game.")
        break

    if valid:
        turn += 1


    if isFull():
        print("Draw")
        break

