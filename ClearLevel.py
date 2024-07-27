from functools import cache
from Gravity import isOnBoardAndValid

#returns a dictionary of the top of the color groups on the left side
#key: row     value: color
def findAllColorGroupOnLeft(app):
    allPixelColorOnLeft = {}
    for i in range(app.rows-1, -1, -1):
        if (i,0) not in app.board:
            break
        else:
            currentColor = app.board[(i, 0)]
        if currentColor == None:
            break
        else:
            if (i-1, 0) in app.board and app.board[(i-1, 0)] == currentColor:
                continue
            else:
                allPixelColorOnLeft[i] = currentColor
    return allPixelColorOnLeft 

#Used simple recursion to check if level is connected
#Also called DFS learned from Lauren Sands
def checkLevelConnected(app, row, col, color, prevDirection = None):
    #the directions are right, up, down; diagonals doesn't counts as connected
    directions = {(0 ,1), (-1, 0), (1, 0)}
    #check if the current pixel is on the right side of the board
    if (row, col) not in app.board or app.board[(row, col)] != color:
        return False
    if (col == (app.cols-1)):
        return True
    else:
        #Erases the opposite of the previous direction so current pixel wouldn't go backwards
        if prevDirection != None:
            pRow, pCol = prevDirection
            directions.remove((-pRow, pCol))
        #Check every direction around the pixel to see if it's the same color
        for drow, dcol in directions:
            newRow = drow+row
            newCol = dcol+col
            result = checkLevelConnected(app, newRow, newCol, color, (drow, dcol))
            if result:
                return True
    return False

def clearLevel(app, row, col, color):
    if row == None:
        return
    pixelsToClear = clearLevelHelper(app, row, col, color)
    for (row,col) in pixelsToClear:
        app.board.pop((row,col))
    return True
        

#BFS learned from Lauren Sands
def clearLevelHelper(app, row, col, color):
    filledCells = set()
    cellsToExplore = [(row, col)]
    directions = [(0 ,1), (0, -1), (1, 0), (-1, 0)]
    
    
    maxNum = 0

    while cellsToExplore != []:
        
        if len(cellsToExplore) > maxNum:
            maxNum = len(cellsToExplore)


        row, col = cellsToExplore.pop(0)
        #check around the cell if any is same color and not in filled Cell
        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]

            filledCells.add((row, col))

            if ((isOnBoard(app, newRow, newCol)) and 
            ((newRow, newCol) not in filledCells) and 
            (app.board.get((newRow, newCol), None) == color)):
                cellsToExplore.append((newRow, newCol))
    print(filledCells)
    print(maxNum)
    return filledCells

def isOnBoard(app, nextRow, nextCol):
    return (0 <= nextRow < app.rows) and (0 <= nextCol  < app.cols)