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
    print('checking level')
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
    pixelsToClear = clearLevelHelper(app, row, col, color)
    for (row,col) in pixelsToClear:
        app.board.remove((row,col))

#BFS learned from Lauren Sands
def clearLevelHelper(app, row, col, color):
    filledCells = {(row, col)}
    cellsToExplore = [(row, col)]
    directions = [(0 ,1), (-1, 0), (1, 0), (0, -1)]

    while cellsToExplore:
        row, col = cellsToExplore.pop(0)
        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]

            if (isOnBoardAndValid(app, newRow, newCol) and 
            (newRow, newCol) not in filledCells and 
            app.board[(newRow, newCol)] == color):
                cellsToExplore.append((newRow, newCol))
                filledCells.add((newRow, newCol))
    return filledCells



# def clearConnectedRow(app, row, col, color):
#     if ((row < 0) or (row >= app.rows) or
#         (col < 0) or (col >= app.cols) or
#         (app.board[(row, col)] == color)):
#         return
#     else:
#         app.board.pop(row, col)
#         clearConnectedRow(app, row + 1, col, color)
#         clearConnectedRow(app, row, col, color)
#         clearConnectedRow(app, row + 1, col + 1, color)
#         clearConnectedRow(app, row, col + 1, color)



# def clearConnectedRow(app):
#     queue = []





# #save all the points of same color to a set to remove later if the level is connected
# coordinatesToRemoveInLevel = set()
# #DFS way to do
# def findAllFloodFillPixels(app, row, col, color):
#     color = app.board.get((row, col), None):
#     if color == None:
#         return False
#     else:
#         findAllFloodFillPixels(app, row, col, color)
#         findAllFloodFillPixels(app, row+1, col, color)
#         findAllFloodFillPixels(app, row, col+1, color)
#         findAllFloodFillPixels(app, row+1, col+1, color)



# def clearConnectedLevels(app):
#     for rowToRemove, colToRemove in coordinatesToRemoveInLevel:
#         app.board.pop((rowToRemove, colToRemove))

# def changeConnectedLevelColor(app):
#     for rowToRemove, colToRemove in coordinatesToRemoveInLevel:
#         app.board[(rowToRemove, colToRemove)] = 'purple'