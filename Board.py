from cmu_graphics import *
from Gravity import *
from Tetrinos import *
from ClearLevel import *

def onAppStart(app):
    #Changing graphic display settings
    app.setMaxShapeCount(30000)
    app.stepsPerSecond = 100
    app.width = 700
    app.height = 700
    boardInformations(app)
    tetrinoInformations(app)
    gravityInformation(app)

#Board information: size, width, height, border width
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

#Tetrino informations: size, color
def tetrinoInformations(app):
    app.tetrinoSize = app.cols//8
    # app.boardWithList = [[None for i in range(app.cols)] for j in range(app.rows)]
    app.tetrinoBoard = [[None for i in range(app.cols//2)] for j in range(app.rows//2)]
    app.currentTetrinoPosition = None
    app.tetrinoColor = 'orange'

def gravityInformation(app):
    #check if the blocks are moving
    app.isSandMoving = False
    app.gravityStepsPerSecond = 0

def gameInformation(app):
    app.paused = False

def drawBoard(app):
    #Doesn't need to draw each grid
    #turns from O(N^2) to O(N)

    # for i in range(app.rows):
    #     for j in range(app.cols):
    #         drawCell(app, i, j)

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

def createSand(app, row, col):
    if app.board.get((row,col)) == None:
        app.isSandMoving = True
        app.board[(row, col)] = app.tetrinoColor

def coordToRowAndCol(app, x, y):
    row = int((y-app.topBoardCoordinate)/app.cellHeight)
    col = int((x-app.leftBoardCoordinate)/app.cellWidth)
    return row, col

def onMouseDrag(app, mouseX, mouseY):
    row, col = coordToRowAndCol(app, mouseX, mouseY)
    createSand(app, row, col)

def onKeyPress(app, key):
    if key == 'a':
        app.isSandMoving = True
        createSand(app, 0, 10)
    if key == 's':
        #returns as (shape, color)
        app.currentTetrinoPosition = getNextPiece(app)
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
    
    #returns a dictionary of the top of the color groups on the left side
    #key: row     value: color
    else:
        levelsToClear = []
        app.gravityStepsPerSecond += 1
        if app.gravityStepsPerSecond%100==0:
            colorGroups = findAllColorGroupOnLeft(app)
            for row in colorGroups.keys():
                color = colorGroups[row]
                if checkLevelConnected(app, row, 0, color):
                    levelsToClear.append((row, color))

        while levelsToClear != []:
            app.paused = True
            print(levelsToClear)
            row, color = levelsToClear[0]
            clearLevel(app, row, 0, color)
            levelsToClear.remove((row, color))

            # for i in range(len(levelsToClear)):
            #     row,color = levelsToClear[i]
            #     clearLevel(app, row, 0, color)
            #     levelsToClear.remove((row, color))
        app.paused = False

def redrawAll(app):
    drawBoard(app)

def main():
    runApp()
main()