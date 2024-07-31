from cmu_graphics import *
from Gravity import *
from Tetrinos import *
from ClearLevel import *
from gameStatus import *
from StartScreen import *
from aboutScreen import *



#Informations and modules
def game_onAppStart(app):
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
    sandInformation(app)
    getNewTetromino(app)

def boardInformations(app):
    app.cols = 40
    app.rows = 2*app.cols
    app.boardWidth = app.width/2
    app.boardHeight = app.height-20
    app.leftBoardCoordinate = app.width//2-(7*app.boardWidth//10)
    app.topBoardCoordinate = app.height//2-(app.boardHeight//2)
    app.cellWidth = app.boardWidth/app.cols
    app.cellHeight = app.boardHeight/app.rows
    app.board = {}
    app.borderWidth = 0.5

def tetrinoInformations(app):
    app.tetrinoSize = app.cols//10
    #stores each coordinates of the tetrino pieces as (row, col, color)
    #only 1 tetrino at a time
    app.tetrinoPiece = []
    app.tetrinoColor = 'red'
    #The small version of rotated Tetrino; not adjusted for size of board
    app.rotatedTetrinoShape = []
    #Expanded rotated Tetrino; adjusted for board size
    app.rotatedTetrinoPiece = []

    #current location 
    app.currRow = 0
    app.currCol = 0

def gravityInformation(app):
    #check if the blocks are moving
    app.isSandMoving = False
    app.gravityStepsPerSecond = 0

def sandInformation(app):
    app.sandStepsPerSecond = 0

def gameInformation(app):
    #game score and level
    app.score = 0
    app.level = 1
    app.linesCleared = 0
    app.highestScore = 0
    app.levelTimesPerSecond = 0
    
    #game status
    app.paused = False
    app.gameOver = False
    
    #sounds
    sandCreedRd = 'SandCreekRd.m4a'
    sussy = 'sussy.m4a'
    app.clearLevelSound = sandCreedRd
    app.gameOverSound = sussy
    app.music = True

def pausedScreenInformation(app):
    #Resume button informations
    app.resumeXCoord = app.boardWidth/2 + app.leftBoardCoordinate
    app.resumeYCoord = 2*app.boardHeight/5 + app.topBoardCoordinate
    app.resumeWidth = 120
    app.resumeHeight = 50

    #New Game button informations
    app.newGameXCoord = app.boardWidth/2 + app.leftBoardCoordinate
    app.newGameYCoord = 3*app.boardHeight/5 + app.topBoardCoordinate
    app.newGameWidthPaused = 180
    app.newGameHeightPaused = 40

    #Music button infromations
    app.musicXCoord = 4*app.boardWidth/5 + app.leftBoardCoordinate
    app.musicYCoord = app.boardHeight/10 + app.topBoardCoordinate
    app.musicWidth = 70
    app.musicHeight = 30

def endScreenInformation(app):
    app.gameOverXCoordEnd = (app.boardWidth/2+app.leftBoardCoordinate)
    app.gameOverYCoordEnd = app.boardHeight/4+app.topBoardCoordinate
    app.newGameYCoordEnd = 3*app.boardHeight/4+app.topBoardCoordinate
    app.newGameWidthEnd = 180
    app.newGameHeightEnd = 40



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
    drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, 
             app.boardHeight, fill = None, border = 'gray', 
             borderWidth = 2*app.borderWidth)

def drawTetromino(app):
    for row, col, color in app.tetrinoPiece:
        drawCell(app, row, col, color)

def drawBackground(app):
    drawRect(0, 0, app.width, app.height, fill = 'black')

def drawPausedScreen(app):
    peru = rgb(205, 133, 63)
    chocolate = rgb(210, 105, 30)
    gray = rgb(43, 43, 40)

    drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, 
             app.boardHeight, fill = gray, opacity = 90)
    #Paused Text
    drawLabel('PAUSED', app.boardWidth/2 + app.leftBoardCoordinate, 
              app.boardHeight/4 + app.topBoardCoordinate, size = 24, 
              fill='white')

    #Resume Button
    drawRect(app.resumeXCoord, 
             app.resumeYCoord, app.resumeWidth, app.resumeHeight, 
             align = 'center', fill = peru)
    drawLabel('RESUME', app.resumeXCoord,
               app.resumeYCoord, bold = True, 
               font='monospace', size = 24)
    
    #New Game Button
    drawRect(app.newGameXCoord, 
             app.newGameYCoord, app.newGameWidthPaused, app.newGameHeightPaused, 
             align = 'center', fill = chocolate)
    drawLabel('NEW GAME', app.newGameXCoord, 
              app.newGameYCoord, bold = True, 
              font='monospace', size = 24)
    
    #Music Button
    drawRect(app.musicXCoord, app.musicYCoord, app.musicWidth, app.musicHeight,
             align = 'center', fill = None, border = 'white')
    drawLabel('MUSIC', app.musicXCoord, app.musicYCoord, fill = 'white')
    if not app.music:
        drawLine(app.musicXCoord - app.musicWidth/2, app.musicYCoord + app.musicHeight/2,
                 app.musicXCoord + app.musicWidth/2, app.musicYCoord - app.musicHeight/2,
                 fill = 'red')

def drawEndScreen(app):
    drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, 
             app.boardHeight, fill = 'black', opacity = 40)

    drawLabel('GAME OVER', app.gameOverXCoordEnd, 
              app.gameOverYCoordEnd, bold = True, 
              font='monospace', size = 30, fill = 'white')


    drawRect(app.gameOverXCoordEnd, app.newGameYCoordEnd, app.newGameWidthEnd, 
             app.newGameHeightEnd, align = 'center', fill = 'white')
    
    drawLabel('New Game', app.gameOverXCoordEnd, app.newGameYCoordEnd, bold = True, 
               font='orbitron', size = 30)

def drawScore(app):
    drawLabel(f'Score: {app.score}', 4*app.width/5, 13*app.width/70, fill = 'white',
              size = 24, bold = True)

def drawLevel(app):
    drawLabel(f'Level: {app.level}', 4*app.width/5, 3*app.height/7, fill = 'white',
              size = 24, bold = True)




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
    if app.score > app.highestScore:
        app.highestScore = app.score
    app.score = 0
    app.level = 0
    app.paused = False
    app.gameOver = False
    getNewTetromino(app)




#Event Handlers
def game_onMousePress(app, mouseX, mouseY):
    #Game Over
    if app.gameOver:
        #New Game
        if ((app.gameOverXCoordEnd - app.newGameWidthEnd/2) < mouseX < (app.gameOverXCoordEnd+app.newGameWidthEnd/2) and 
            (app.newGameYCoordEnd - app.newGameHeightEnd/2) < mouseY < (app.newGameYCoordEnd+app.newGameHeightEnd/2)):
            setActiveScreen('startScreen')
    
    #Paused
    if app.paused and not app.gameOver:
        #Mouse in paused button
        if ((app.resumeXCoord - app.resumeWidth/2) < mouseX < (app.resumeWidth/2 + app.resumeXCoord) and 
            (app.resumeYCoord - app. resumeHeight/2) < mouseY < (app.resumeYCoord + app.resumeHeight/2)):
            app.paused = not app.paused
        
        #Mouse in new game button
        elif ((app.gameOverXCoordEnd - app.gameOverXCoordEnd/2) < mouseX < (app.gameOverXCoordEnd + app.gameOverXCoordEnd/2) and 
            (app.newGameYCoord - app.newGameYCoordEnd/2) < mouseY < (app.newGameYCoordEnd + app.newGameYCoordEnd/2)):
            resetGame(app)

        #mouse in music button
        elif (((app.musicXCoord - app.musicWidth) < mouseX < (app.musicXCoord + app.musicWidth/2)) and 
              ((app.musicYCoord - app.musicHeight/2) < mouseY < (app.musicYCoord + app.musicHeight/2))):
            app.music = not app.music

def game_onMouseDrag(app, mouseX, mouseY):
    row, col = coordToRowAndCol(app, mouseX, mouseY)
    createSand(app, row, col)

def game_onKeyPress(app, key):
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
        rotatedPiece = rotate2dListClockwise(app.rotatedTetrinoShape)
        turnPieceShapeToCoord(app, rotatedPiece, app.tetrinoColor)
        app.rotatedTetrinoShape = rotatedPiece

    if key == 'space':
        while moveTetromino(app, 1, 0):
            pass

def game_onKeyHold(app, keys):
    if not app.paused:
        if 'down' in keys:
            app.score += 1
            moveTetromino(app, 1, 0)

        if 'left' in keys:
            moveTetromino(app, 0, -1)

        if 'right' in keys:
            moveTetromino(app, 0, 1)

def game_onStep(app):    
    if not app.paused:
        #lower the rate of checking connected rows so program can be faster 
        #formula divides by tetrino size; checks rows when there are no gaps between blocks
        app.gravityStepsPerSecond += 1
        print(app.gravityStepsPerSecond)
        if app.gravityStepsPerSecond%(2*app.tetrinoSize)==0:
            # if not app.isSandMoving:
            checkAndClearConnectedRows(app)
            #move row down 1 row and 0 col
        moveSandsDown(app)
        moveTetromino(app, 1, 0)
    #level increases by 1 every 10 seconds
    app.levelTimesPerSecond += 1
    if app.levelTimesPerSecond % (app.stepsPerSecond*10) == 0 and not app.paused:
        app.level+=1

def game_redrawAll(app):
    drawBackground(app)
    drawScore(app)
    drawLevel(app)
    drawTetromino(app)
    drawBoard(app)
    if app.gameOver:
        drawEndScreen(app)
    if app.paused and not app.gameOver:
        drawPausedScreen(app)

def main():
    runAppWithScreens(initialScreen='startScreen')
main()