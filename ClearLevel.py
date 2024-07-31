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

#DFS with stack learned from Lauren Sands
#given row and col is the top block of a color group
def checkLevelConnected(app, row, col, color):
    filledCells = set()
    cellsToExplore = [(row, col)]
    #if the cell is already in cells to explore, no need to add it again and check it again
    #checking if the cell already in the explore list is faster when a set of same elements exist
    cellsToExploreSet = set((row,col))
    directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    while cellsToExplore != []:
        currRow, currCol = cellsToExplore.pop()
        if currCol == app.cols-1:
            return True
        #check around the cell if any is same color and not in filled Cell
        for direction in directions:
            newRow = currRow + direction[0]
            newCol = currCol + direction[1]
            if ((isOnBoard(app, newRow, newCol)) and 
            ((newRow, newCol) not in filledCells) and 
            (app.board.get((newRow, newCol), None) == color) and
            ((newRow, newCol) not in cellsToExploreSet)):
                cellsToExplore.append((newRow, newCol))
                cellsToExploreSet.add((newRow, newCol))
    return False

def clearLevel(app, row, col, color):
    if row == None:
        return
    # app.clearLevelSound.play()
    pixelsToClear = clearLevelHelper(app, row, col, color)
    app.score += len(pixelsToClear)
    for (row,col) in pixelsToClear:
        app.board.pop((row,col))
    return True
        
#BFS with stack learned from Lauren Sands
def clearLevelHelper(app, row, col, color):
    filledCells = set()
    cellsToExplore = [(row, col)]
    #if the cell is already in cells to explore, no need to add it again and check it again
    #checking if the cell already in the explore list is faster when a set of same elements exist
    cellsToExploreSet = set((row,col))
    directions = [(0 ,1), (1, 0), (-1, 0), (0, -1)]
    while cellsToExplore != []:
        currRow, currCol = cellsToExplore.pop(0)
        #check around the cell if any is same color and not in filled Cell
        filledCells.add((currRow, currCol))
        for direction in directions:
            newRow = currRow + direction[0]
            newCol = currCol + direction[1]
            if ((isOnBoard(app, newRow, newCol)) and 
            ((newRow, newCol) not in filledCells) and 
            (app.board.get((newRow, newCol), None) == color) and
            ((newRow, newCol) not in cellsToExploreSet)):
                cellsToExplore.append((newRow, newCol))
                cellsToExploreSet.add((newRow, newCol))
    return filledCells

def isOnBoard(app, nextRow, nextCol):
    return (0 <= nextRow < app.rows) and (0 <= nextCol < app.cols)

def checkAndClearConnectedRows(app):
    levelsToClear = []
    #checking each color groups if they're connected
    colorGroups = findAllColorGroupOnLeft(app)
    for row in colorGroups.keys():
        color = colorGroups[row]
        if checkLevelConnected(app, row, 0, color):
            levelsToClear.append((row, color))

    #clear the connected rows
    while levelsToClear != []:
        app.paused = True
        row, color = levelsToClear[0]
        clearLevel(app, row, 0, color)
        levelsToClear.remove((row, color))
    app.paused = False