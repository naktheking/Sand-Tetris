from cmu_graphics import *
from Gravity import *
from Tetrinos import *
from ClearLevel import *


#Informations and modules
def onAppStart(app):
    #Changing graphic display settings
    app.setMaxShapeCount(30000)
    app.stepsPerSecond = 20
    app.width = 700
    app.height = 700
    boardInformations(app)
    tetrinoInformations(app)
    gravityInformation(app)
    gameInformation(app)
    pausedScreenInformation(app)
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
    app.borderWidth = 0.5
def tetrinoInformations(app):
    app.tetrinoSize = app.cols//10
    #stores each coordinates of the tetrino pieces as (row, col, color)
    #only 1 tetrino at a time
    app.tetrinoPiece = []
    app.tetrinoColor = 'red'
    app.tetrinoStepsPerSecond = 0
def gravityInformation(app):
    #check if the blocks are moving
    app.isSandMoving = False
    app.gravityStepsPerSecond = 0
def gameInformation(app):
    app.paused = False
    app.gameOver = False
def pausedScreenInformation(app):
    app.resumeLeftCoord = 290
    app.resumeTopCoord = 247
    app.resumeWidth = 120
    app.resumeHeight = 40

    app.newGameLeftCoord = 275
    app.newGameTopCoord = 383
    app.newGameWidth = 150
    app.newGameHeight = 40
    
#Drawing
def drawBoard(app):
    for row, col in app.board:
        drawCell(app, row, col, app.board[(row, col)])
    drawBoardBorder(app)

def drawCell(app, row, col, color = None):
    cellLeft = app.leftBoardCoordinate + col*app.cellWidth
    cellTop = app.topBoardCoordinate + row*app.cellHeight
    drawRect(cellLeft, cellTop, app.cellWidth, app.cellHeight, fill = color, 
             border = None)

def drawBoardBorder(app):
    drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, app.boardHeight,
             fill = None, border = 'gray', borderWidth = 2*app.borderWidth)

def drawTetromino(app):
    for row, col, color in app.tetrinoPiece:
        drawCell(app, row, col, color)

def drawBackground(app):
    drawRect(0, 0, app.width, app.height, fill = None)

def drawPausedScreen(app):
    drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, app.boardHeight, fill = 'black', opacity = 75)
    drawRect(app.boardWidth/2 + app.leftBoardCoordinate, 2*app.boardHeight/5, 120, 50, align = 'center', fill = 'gray')
    drawLabel('resume', app.boardWidth/2 + app.leftBoardCoordinate, 2*app.boardHeight/5, bold = True, font='monospace', 
               size = 24)
    drawRect(app.boardWidth/2 + app.leftBoardCoordinate, 3*app.boardHeight/5, 150, 50, align = 'center', fill = 'gray')
    drawLabel('new game', app.boardWidth/2 + app.leftBoardCoordinate, 3*app.boardHeight/5, bold = True, font='monospace', 
               size = 24)


#Functions
def checkAndClearConnectedRows(app):
    levelsToClear = []
    #slow the run speed down 10 times
    app.gravityStepsPerSecond += 1
    if app.gravityStepsPerSecond%10==0:
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

def resetGame(app):
    app.board = {}
    app.tetrinoPiece = []
    app.paused = not app.paused
    getNewTetromino(app)


#Event Handlers

# def onMouseMove(app, mouseX, mouseY):
#     if (app.resumeLeftCoord < mouseX < app.resumeWidth + app.resumeLeftCoord and 
#         app.resumeTopCoord < mouseY < app.resumeTopCoord + app.resumeHeight):
#         app.paused = not app.paused
#     if (app.newGameLeftCoord < mouseX < app.newGameLeftCoord + app.newGameWidth and 
#         app.newGameTopCoord < mouseY < app.newGameTopCoord + app.newGameHeight):
#         resetGame(app)

def onMousePress(app, mouseX, mouseY):
    if (app.resumeLeftCoord < mouseX < app.resumeWidth + app.resumeLeftCoord and 
        app.resumeTopCoord < mouseY < app.resumeTopCoord + app.resumeHeight):
        app.paused = not app.paused
    if (app.newGameLeftCoord < mouseX < app.newGameLeftCoord + app.newGameWidth and 
        app.newGameTopCoord < mouseY < app.newGameTopCoord + app.newGameHeight):
        resetGame(app)

def onMouseDrag(app, mouseX, mouseY):
    row, col = coordToRowAndCol(app, mouseX, mouseY)
    createSand(app, row, col)

def onKeyPress(app, key):
    if key == 'a':
        app.isSandMoving = True
        createSand(app, 0, 10)
    if key == 's':
        getNewTetromino(app)
    if key == 'p':
        app.paused = not app.paused

    if key == '0':
        app.tetrinoColor = TetrinoColors[0]
    elif key == '1':
        app.tetrinoColor = TetrinoColors[1]
    elif key == '2':
        app.tetrinoColor = TetrinoColors[2]
    elif key == '3':
        app.tetrinoColor = TetrinoColors[3]

def onKeyHold(app, keys):
    if 'down' in keys:
        moveTetromino(app, 1, 0)

    if 'left' in keys:
        moveTetromino(app, 0, -1)

    if 'right' in keys:
        moveTetromino(app, 0, 1)

def onStep(app):
    #if sand is not moving, no need to move it down; Saves time for checking
    if not app.paused:
        #move row down 1 row and 0 col
        moveTetromino(app, 1, 0)
        moveSandsDown(app)
        checkAndClearConnectedRows(app)

def redrawAll(app):
    drawBackground(app)
    drawTetromino(app)
    drawBoard(app)
    if app.paused:
        drawPausedScreen(app)

def main():
    runApp()
main()