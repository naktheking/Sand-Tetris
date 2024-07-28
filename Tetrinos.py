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

