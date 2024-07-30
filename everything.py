from cmu_graphics import *
import random

#Informations and modules
def onAppStart(app):
    #Changing graphic display settings
    app.setMaxShapeCount(30000)
    app.stepsPerSecond = 50
    app.width = 700
    app.height = 700
    boardInformations(app)
    tetrinoInformations(app)
    gravityInformation(app)
    gameInformation(app)
def boardInformations(app):
    app.cols = 24
    app.rows = 2*app.cols
    app.boardWidth = app.width/2
    app.boardHeight = app.height-20
    app.leftBoardCoordinate = app.width//2-(app.boardWidth//2)
    app.topBoardCoordinate = app.height//2-(app.boardHeight//2)
    app.cellWidth = app.boardWidth/app.cols
    app.cellHeight = app.boardHeight/app.rows
    # app.boardWithList = [[None for i in range(app.cols)] for j in range(app.rows)]
    #app.board is a dictionary; keys are the coordinates; values are the color
    app.board = {}
    app.borderWidth = 0.2
def tetrinoInformations(app):
    app.tetrinoSize = app.cols//10
    app.tetrinoBoard = [[None for i in range(app.cols//2)] for j in range(app.rows//2)]
    app.currentTetrinoPosition = None
    app.tetrinoColor = 'orange'
def gravityInformation(app):
    #check if the blocks are moving
    app.isSandMoving = False
    app.gravityStepsPerSecond = 0
def gameInformation(app):
    app.paused = False
    app.gameOver = False


#Drawing
def drawBoard(app):
    for row, col in app.board:
        drawCell(app, row, col, app.board[(row, col)])
    drawBoardBorder(app)

def drawCell(app, row, col, color = None):
    cellLeft = app.leftBoardCoordinate + col*app.cellWidth
    cellTop = app.topBoardCoordinate + row*app.cellHeight
    drawRect(cellLeft, cellTop, app.cellWidth, app.cellHeight, fill = color, 
             border = 'black', borderWidth = app.borderWidth)

def drawBoardBorder(app):
    drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, app.boardHeight,
             fill = None, border = 'gray', borderWidth = 2*app.borderWidth)

def drawTetromino(app):
    piece, color = getNextPiece(app)
    lengthOfRow, lengthOfCol = piece.getLengthOfRow(), piece.getLengthOfCol()
    for row in range(lengthOfRow):
        for col in range(lengthOfCol):    
                if piece.checkCondition(row, col) == True:
                    for innerRow in range(app.tetrinoSize):
                        for innerCol in range(app.tetrinoSize):
                            app.board[((row * app.tetrinoSize + innerRow), (col * app.tetrinoSize + innerCol + app.cols//2))] = color
    app.isSandMoving = True

def getStartingTetrominoSpot(app, piece):
    pass


#Functions
def checkAndClearConnectedRows(app):
    levelsToClear = []
    #slow the run speed down 10 times
    app.gravityStepsPerSecond += 1
    if app.gravityStepsPerSecond%20==0:
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

def createSand(app, row, col):
    if app.board.get((row,col)) == None:
        app.isSandMoving = True
        app.board[(row, col)] = app.tetrinoColor

def coordToRowAndCol(app, x, y):
    row = int((y-app.topBoardCoordinate)/app.cellHeight)
    col = int((x-app.leftBoardCoordinate)/app.cellWidth)
    return row, col


#Event Handlers; Controllers
def onMouseDrag(app, mouseX, mouseY):
    row, col = coordToRowAndCol(app, mouseX, mouseY)
    createSand(app, row, col)

def onKeyPress(app, key):
    if key == 'a':
        app.isSandMoving = True
        createSand(app, 0, 10)
    if key == 's':
        drawTetromino(app)
    if key == '0':
        app.tetrinoColor = TetrinoColors[0]
    elif key == '1':
        app.tetrinoColor = TetrinoColors[1]
    elif key == '2':
        app.tetrinoColor = TetrinoColors[2]
    elif key == '3':
        app.tetrinoColor = TetrinoColors[3]

def onStep(app):
    #if sand is not moving, no need to move it down; Saves time for checking
    if app.isSandMoving == True and app.paused == False:
        moveSandsDown(app)
    else:
        checkAndClearConnectedRows(app)
    
def redrawAll(app):
    drawBoard(app)

def main():
    runApp()

main()




#Tetrimino File
class TetrinosPieces():
    #shape is a 2d list with True being the pixel exists and False if it doesn't
    def __init__(self, shape):
        self.shape = shape
    
    def checkCondition(self, row, col):
        if row > len(self.shape) or col > len(self.shape[0]):
            return False
        return self.shape[row][col]  

    def getLengthOfRow(self):
        return len(self.shape)
    
    def getLengthOfCol(self):
        return len(self.shape[0])
    


# Define each Tetrimino piece
ipiece = TetrinosPieces([[True, True, True, True]])
jpiece = TetrinosPieces([[True, False, False],
                         [True, True, True]])
lpiece = TetrinosPieces([[False, False, True],
                         [True, True, True]])
opiece = TetrinosPieces([[True, True],
                         [True, True]])
spiece = TetrinosPieces([[False, True, True],
                         [True, True, False]])
tpiece = TetrinosPieces([[False, True, False],
                         [True, True, True]])
zpiece = TetrinosPieces([[True, True, False],
                         [False, True, True]])
# Add all pieces to a list
allTetrinoPieces = [ipiece, jpiece, lpiece, opiece, spiece, tpiece, zpiece]
#Tetrino colors
TetrinoColors = ['red', 'green', 'yellow', 'blue']



def contact(app, piece, row, col):
    bottomRow = piece.shape[-1]
    piece.getLength



#code copied from previous csacademy assignment

# def rotate2dListClockwise(L):
#     M = []
#     for j in range(len(L[0])):
#         list = []
#         for i in range(len(L)-1,-1,-1):
#             list.append(L[i][j])
#         M.append(list)
#     return M

# def rotatePieceClockwise(app):
#     oldPiece = app.piece
#     oldTopRow = app.pieceTopRow
#     oldLeftCol = app.pieceLeftCol

#     app.piece = rotate2dListClockwise(app.piece)

#     centerRow = oldTopRow + len(oldPiece)//2
#     centerCol = oldLeftCol + len(oldPiece[0])//2


#     newRows = len(app.piece)
#     app.pieceTopRow = centerRow - newRows//2
    
#     newCol = len(app.piece[0])
#     app.pieceLeftCol = centerCol - newCol//2

#     if not pieceIsLegal(app):
#         app.piece = oldPiece
#         app.pieceTopRow = oldTopRow
#         app.pieceLeftCol = oldLeftCol



#returns a random selection of a tetrino piece and a random tetrino color in a tuple
def getNextPiece(app):
    return (random.choice(allTetrinoPieces), random.choice(TetrinoColors))



#Gravity File
import random

#check if the next position of the block is valid and legal
def isOnBoardAndValid(app, nextRow, nextCol):
    if nextRow >= app.rows or nextCol < 0 or nextCol >= app.cols or (nextRow, nextCol) in app.board:
        return False
    return True

#move each sand particle down
def moveSandsDown(app):
    #establishing directions and positions to remove once inside the for loop
    direction = [(1, -1), (1, +1)]
    valuesToRemove = set()
    valuesToAdd = set()

    #looping through each coordinate of sand and go down one if the spot below is empty
    for row, col in app.board:
        color = app.board.get((row, col))
        if isOnBoardAndValid(app, row+1, col):
            #add the values to a set to remove it after the loop
            #also add the new value to another set to add it after the loop
            valuesToRemove.add((row, col))
            valuesToAdd.add((row+1, col, color))
        else:
            #samething but to leftbottom and rightbottom directions if direct bottom is filled
            drow, dcol = random.choice(direction)
            newRow = drow + row
            newCol = dcol + col
            if isOnBoardAndValid(app, newRow, newCol):
                valuesToAdd.add((newRow, newCol, app.board[(row, col)]))
                valuesToRemove.add((row, col))
    
    #change if sand is moving; if it is we will change it later when adding new values 
    #if not changed later, it will remain false
    app.isSandMoving = False
    #add values to dictionary from set
    for keys in valuesToAdd:
        lrow, rcol, rcolor = keys
        app.board[(lrow, rcol)] = rcolor
        #change to show that sand is moving
        app.isSandMoving = True

    #removing values to dictionary from set
    for keys in valuesToRemove:
        lrow, lcol = keys
        app.board.pop((lrow, lcol))

def moveTetrinosDown(app):
    pass


#clear line file
from functools import cache

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