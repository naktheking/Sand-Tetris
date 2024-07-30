from cmu_graphics import *
from Gravity import *
from Tetrinos import *
from ClearLevel import *
from gameStatus import *


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
    endScreenInformation(app)
def boardInformations(app):
    app.cols = 40
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
def endScreenInformation(app):
    app.newGameLeft, app.newGameTop = 250, 398
    app.newGameWidth, app.newGameHeight = 200, 40





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
    drawRect(0, 0, app.width, app.height, fill = 'black')

def drawPausedScreen(app):
    peru = rgb(205, 133, 63)
    chocolate = rgb(210, 105, 30)
    gray = rgb(43, 43, 40)

    drawRect(0, 0, app.width, app.height, fill = gray, opacity = 50)
    
    drawLabel('PAUSED',app.width/2, app.height/5, size = 24, fill='white')

    drawRect(app.width/2, 2*app.height/5, 120, 50, align = 'center', fill = peru)
    drawLabel('RESUME', app.width/2, 2*app.height/5, bold = True, font='monospace', 
               size = 24)
    
    drawRect(app.width/2, 3*app.height/5, 150, 50, align = 'center', fill = chocolate)
    drawLabel('NEW GAME', app.width/2, 3*app.height/5, bold = True, font='monospace', 
               size = 24)

def drawEndScreen(app):
    drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, 
             app.boardHeight, fill = 'black', opacity = 70)

    drawLabel('GAME OVER', app.boardWidth/2+app.leftBoardCoordinate, 
              app.boardHeight/4+app.topBoardCoordinate, bold = True, 
              font='monospace', size = 30, fill = 'white')


    drawRect(app.boardWidth/2+app.leftBoardCoordinate,
             3*app.boardHeight/5+app.topBoardCoordinate, 200, 40, align = 'center', 
             fill = 'white')
    drawLabel('New Game', app.boardWidth/2+app.leftBoardCoordinate,
               3*app.boardHeight/5+app.topBoardCoordinate, bold = True, 
               font='orbitron', size = 30)



#Functions

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
    app.paused = False
    app.gameOver = False
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
    if app.gameOver:
        if (app.newGameLeft < mouseX < app.newGameLeft+app.newGameWidth and 
            app.newGameTop < mouseY < app.newGameTop+app.newGameHeight):
            resetGame(app)
    
    if app.paused and not app.gameOver:
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
    if key == 's':
        getNewTetromino(app)
    elif key == 'p':
        app.paused = not app.paused

    if key == '0':
        app.tetrinoColor = TetrinoColors[0]
    elif key == '1':
        app.tetrinoColor = TetrinoColors[1]
    elif key == '2':
        app.tetrinoColor = TetrinoColors[2]
    elif key == '3':
        app.tetrinoColor = TetrinoColors[3]

    if key == 'up':
        rotate2dListClockwise(app.tetrinoPiece)
        print(app.tetrinoPiece)

def onKeyHold(app, keys):
    if not app.paused:
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
    if app.gameOver:
        drawEndScreen(app)
    if app.paused and not app.gameOver:
        drawPausedScreen(app)

def main():
    runApp()
main()