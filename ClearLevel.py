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
    print('Amount of pixels connected ',len(pixelsToClear))
    for (row,col) in pixelsToClear:
        app.board.pop((row,col))
    return True
        

#BFS learned from Lauren Sands
@cache
def clearLevelHelper(app, row, col, color):
    filledCells = set()
    cellsToExplore = [(row, col)]
    directions = [(0 ,1), (0, -1), (1, 0), (-1, 0)]
    #efficiency test
    maxNum = 0
    
    
    
    
    while cellsToExplore != []:      





        #seeing how efficent code it: will delete later
        if len(cellsToExplore) > maxNum:
            maxNum = len(cellsToExplore)





        currRow, currCol = cellsToExplore.pop(0)
        # print('cells to explore', cellsToExplore)
        # print('current row and col',row, col)
        # print('------')
        #check around the cell if any is same color and not in filled Cell
        filledCells.add((currRow, currCol))

        for direction in directions:
            newRow = currRow + direction[0]
            newCol = currCol + direction[1]
            print('1st row and col to compare',newRow, newCol)
            print('--------')
            print((isOnBoard(app, newRow, newCol)))
            print(((newRow, newCol) not in filledCells))
            print((app.board.get((newRow, newCol), None) == color))
            print('--------')
            # print((isOnBoard(app, newRow, newCol)) and 
            # ((newRow, newCol) not in filledCells) and 
            # (app.board.get((newRow, newCol), None) == color))

            if ((isOnBoard(app, newRow, newCol)) and 
            ((newRow, newCol) not in filledCells) and 
            (app.board.get((newRow, newCol), None) == color)):
                
                print('2nd row and col to compare',newRow, newCol)
                cellsToExplore.append((newRow, newCol))
    
    # print(filledCells)
    print(maxNum)




    return filledCells

def isOnBoard(app, nextRow, nextCol):
    return (0 <= nextRow < app.rows) and (0 <= nextCol < app.cols)