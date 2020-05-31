from random import seed
from random import randint

#TODO
# split up methods in to own files
# make a basic AI
# push stats out of changed boards(???)
#

#-----------------
# General flow to play
# loop start
# roll dice (DONE)
# generate all possible moves + boards (DONE)
# Ai Choice
# apply move
# has other player won 
# Other players turn
# loop 
#----------------
# board will a array of ints with one player beign - and the other +
board = []
plusPlayerTaken = 0
minusPlayerTaken = 0

#start positions for a back gammon game
def getNewBoard():
    return [-2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 2]


# assumes diceRoll is a array [,] or same number 4 times
def diceRolls():
    value1 = randint(1, 6)
    value2 = randint(1, 6)
    if(value1 == value2):
        return [value1, value1, value1, value1]
    return [value1, value2]

#TODO make so player generator uses a multipler for + or - 
#will return all possible moves from current board using amount piece can move
def generateAllPossibelCombinationsNormalPlay(player, currentBoard, amountToMove):
    possibleCombinations = []
    allPiecesInLastQuarter = True
    # curretnly will only work for player -1
    for index, valueCurrentPosition in enumerate(currentBoard, start=0):
        if(player == -1 and not index > (len(currentBoard)/4)*3-1 or player == +1 and not index < len(currentBoard)/4-1):
            atPlayersPiece = 0 > valueCurrentPosition
            if (atPlayersPiece):
                allPiecesInLastQuarter = False

    for index, valueCurrentPosition in enumerate(currentBoard, start=0):
        atPlayersPiece = 0 > valueCurrentPosition

        if(atPlayersPiece):
            if (player == -1):
                movingToPosition = index+amountToMove
                moveOffBoard = not movingToPosition < (len(currentBoard))
            else:
                movingToPosition = index-amountToMove
                moveOffBoard = movingToPosition < 0
            if (player == -1):
                if (not moveOffBoard):
                    movingTospaceEmptyMovingTo = currentBoard[movingToPosition] == 0
                    movingToPlayersTokenValid = (
                        currentBoard[movingToPosition] < 0 and currentBoard[movingToPosition] > -5)
                    canTakePiece = currentBoard[movingToPosition] == +1
                    # normal move
                    if(movingTospaceEmptyMovingTo or movingToPlayersTokenValid):
                        edittedBoard = currentBoard.copy()
                        edittedBoard[movingToPosition] = edittedBoard[movingToPosition] - 1
                        edittedBoard[index] = edittedBoard[index] + 1
                        possibleCombinations.append(edittedBoard.copy())
                    # take move
                    if(canTakePiece):
                        edittedBoard = currentBoard.copy()
                        edittedBoard[movingToPosition] = -1
                        edittedBoard[index] = edittedBoard[index] + 1
                        possibleCombinations.append(edittedBoard.copy())
                # movign off board move
                if (moveOffBoard and allPiecesInLastQuarter):
                    edittedBoard = currentBoard.copy()
                    edittedBoard[index] = edittedBoard[index] + 1
                    possibleCombinations.append(edittedBoard.copy())
            if (player == +1):
                if (not moveOffBoard):
                    movingTospaceEmptyMovingTo = currentBoard[movingToPosition] == 0
                    movingToPlayersTokenValid = (
                        currentBoard[movingToPosition] > 0 and currentBoard[movingToPosition] < +5)
                    canTakePiece = currentBoard[movingToPosition] == -1
                    # normal move
                    if(movingTospaceEmptyMovingTo or movingToPlayersTokenValid):
                        edittedBoard = currentBoard.copy()
                        edittedBoard[movingToPosition] = edittedBoard[movingToPosition] + 1
                        edittedBoard[index] = edittedBoard[index] - 1
                        possibleCombinations.append(edittedBoard.copy())
                    # take move
                    if(canTakePiece):
                        edittedBoard = currentBoard.copy()
                        edittedBoard[movingToPosition] = +1
                        edittedBoard[index] = edittedBoard[index] - 1
                        possibleCombinations.append(edittedBoard.copy())
                        # movign off board move
                if (moveOffBoard and allPiecesInLastQuarter):
                    edittedBoard = currentBoard.copy()
                    edittedBoard[index] = edittedBoard[index] - 1
                    possibleCombinations.append(edittedBoard.copy())
    return possibleCombinations



#generates froma  dice roll all possible boards
def allPossibleBoards(player, currentBoard, diceRolls):
    output = []
    # if a double
    if (len(diceRolls) == 4):
        possibleBoards1 = generateAllPossibelCombinationsNormalPlay(
            player, currentBoard, diceRolls[0])
        for board in possibleBoards1:
            possibleBoards2 = generateAllPossibelCombinationsNormalPlay(
                player, board, diceRolls[0])
            for board in possibleBoards2:
                possibleBoards3 = generateAllPossibelCombinationsNormalPlay(
                    player, board, diceRolls[0])
                for board in possibleBoards3:
                    possibleBoards4 = generateAllPossibelCombinationsNormalPlay(
                        player, board, diceRolls[0])
                    for board in possibleBoards4:
                        output.append(board.copy())
    # everything Else
    else:
        possibleBoards1 = generateAllPossibelCombinationsNormalPlay(
            player, currentBoard, diceRolls[0])
        for board in possibleBoards1:
            possibleBoards2 = generateAllPossibelCombinationsNormalPlay(
                player, currentBoard, diceRolls[1])
            for board in possibleBoards2:
                output.append(board.copy())
        possibleBoards1 = generateAllPossibelCombinationsNormalPlay(
            player, currentBoard, diceRolls[1])
        for board in possibleBoards1:
            possibleBoards2 = generateAllPossibelCombinationsNormalPlay(
                player, currentBoard, diceRolls[0])
            for board in possibleBoards2:
                output.append(board.copy())

    return output
    # remove dupicatess


# -----------------
seed(1)
currentBoard = getNewBoard()

for val in allPossibleBoards(-1, currentBoard, [1, 2]):
    print(val)


