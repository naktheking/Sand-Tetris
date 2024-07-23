from functools import cache
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
    
    #returns a dictionary of the top of the color groups on the left side
    #key: row     value: color
    return allPixelColorOnLeft 

coordinatesToRemoveInLevel = set()

def checkLevelConnected(app, row, col, color, prevDirection = None):
    #the directions are right, up, down; diagonals doesn't counts as connected
    directions = {(0 ,1), (-1, 0), (1, 0)}
    #check if the current pixel is on the right side of the board
    if (row, col) not in app.board or app.board[(row, col)] != color:
        return False
    if (col == (app.cols-1)):
        coordinatesToRemoveInLevel.add((row, col))
        return True
    
    else:
        if prevDirection != None:
            pRow, pCol = prevDirection
            directions.remove((-pRow, pCol))
        for drow, dcol in directions:
            newRow = drow+row
            newCol = dcol+col
            result = checkLevelConnected(app, newRow, newCol, color, (drow, dcol))
            if result:
                coordinatesToRemoveInLevel.add((newRow, newCol))
                return True
    return False