import random
from Gravity import isOnBoardAndValid
from gameStatus import *


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
    
    def __repr__(self):
        return str(self.shape)

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

#check if tetromino contacts with current sand blocks
#the +1 and -1 is there becuase row and col starts at 1 but dictionary coordiantes start at 0
def tetrominoContact(app, tetrominoCoords):
    for row, col, _ in tetrominoCoords:
        if ((row+1, col) in app.board) or (row == app.rows-1):
            return True
    return False

#chooses a random tetrimino piece and a random color
#then scale it proportion to the board and add it to the app.tetrino list
def getNewTetromino(app):
    piece, color = getNextPiece()
    turnPieceToCoord(app, piece, color)

def turnPieceToCoord(app, piece, color):
    startCol = ((app.cols-piece.getLengthOfCol())//2)
    lengthOfRow, lengthOfCol = piece.getLengthOfRow(), piece.getLengthOfCol()
    for row in range(lengthOfRow):
        for col in range(lengthOfCol):    
                if piece.checkCondition(row, col) == True:
                    for innerRow in range(app.tetrinoSize):
                        for innerCol in range(app.tetrinoSize):
                            app.tetrinoPiece.append(((row * app.tetrinoSize + innerRow), (col * app.tetrinoSize + innerCol + startCol), color))
    app.isSandMoving = True


#moves each piece of the tetromino down by 1
#check if it tounches the board
#if it does, turn everything into sands and spawn a new piece
def moveTetromino(app, drow, dcol):
    newTetrinoPiece = []
    
    for i in range(len(app.tetrinoPiece)):
        row, col, color = app.tetrinoPiece[i]
        newRow, newCol = row+drow, col+dcol

        if isOnBoardAndValid(app, newRow, newCol):
            newTetrinoPiece.append((newRow, newCol, color))
        
        #Went off the board, either too left or too right
        else:
            newTetrinoPiece = []
            #if the block is too left, change in cols would be the distance from 
            #the left most column of the tetrino to the edge
            if newCol < 0:
                leftCol = getLeftmostCol(app)
                for row, col, color in app.tetrinoPiece:
                    newRow = row+drow
                    newTetrinoPiece.append((newRow, col-leftCol, color))
            #same thing with the right side but it should be the right edge - right most column
            if newCol >= app.cols:
                rightCol = getRightmostCol(app)
                dCol = app.cols-rightCol-1
                for row, col, color in app.tetrinoPiece:
                    newRow = row+drow
                    newTetrinoPiece.append((newRow, col + dCol, color))            
            break

    app.tetrinoPiece = newTetrinoPiece

    if tetrominoContact(app, app.tetrinoPiece):
        for row, col, color in app.tetrinoPiece:
            app.board[(row, col)] = color
        app.tetrinoPiece = []
        getNewTetromino(app)
        checkGameOver(app)


#rotates tetromino clockwise
def rotate2dListClockwise(L):
    M = []
    for j in range(len(L[0])):
        list = []
        for i in range(len(L)-1,-1,-1):
            list.append(L[i][j])
        M.append(list)
    return M

#returns a random selection of a tetrino piece and a random tetrino color in a tuple
def getNextPiece():
    return (random.choice(allTetrinoPieces), random.choice(TetrinoColors))

def getRightmostCol(app):
    maxCol = None
    for row, col, color in app.tetrinoPiece:
        if maxCol == None or col > maxCol:
            maxCol = col
    return maxCol
def getLeftmostCol(app):
    minCol = None
    for row, col, color in app.tetrinoPiece:
        if minCol == None or col < minCol:
            minCol = col
    return minCol