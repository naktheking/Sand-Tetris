import random

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

#check if tetromino contacts with current sand blocks
def tetrominoContact(app, tetrominoCoords):
    for row, col, color in tetrominoCoords:
        if (row, col) in app.board:
            return True
        else:
            return False



#chooses a random tetrimino piece and a random color
#then scale it proportion to the board and add it to the app.tetrino list
def getNewTetromino(app):
    piece, color = getNextPiece()
    startCol = ((app.cols-piece.getLengthOfCol())//2)
    lengthOfRow, lengthOfCol = piece.getLengthOfRow(), piece.getLengthOfCol()
    for row in range(lengthOfRow):
        for col in range(lengthOfCol):    
                if piece.checkCondition(row, col) == True:
                    for innerRow in range(app.tetrinoSize):
                        for innerCol in range(app.tetrinoSize):
                            app.tetrinoPiece.append(((row * app.tetrinoSize + innerRow), (col * app.tetrinoSize + innerCol + startCol), color))
    app.isSandMoving = True

def moveTetromino(app):
    for i in range(len(app.tetrinoPiece)):
        row, col, color = app.tetrinoPiece[i]
        app.tetrinoPiece[i] = (row+1, col, color)

    if tetrominoContact(app, app.tetrinoPiece):
        for row, col, color in app.tetrinoPiece:
            app.board[(row-1, col)] = color
        app.tetrinoPiece = []
        getNewTetromino(app)


#returns a random selection of a tetrino piece and a random tetrino color in a tuple
def getNextPiece():
    return (random.choice(allTetrinoPieces), random.choice(TetrinoColors))