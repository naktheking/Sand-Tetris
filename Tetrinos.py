import random

class TetrinosPieces():
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
    
# Define each Tetrimino piece
ipiece = TetrinosPieces('ipiece', [(0, 0), (0, 1), (0, 2), (0, 3)])
jpiece = TetrinosPieces('jpiece', [(0, 0), (1, 0), (1, 1), (1, 2)])
lpiece = TetrinosPieces('lpiece', [(1, 0), (1, 1), (1, 2), (0, 2)])
opiece = TetrinosPieces('opiece', [(0, 0), (0, 1), (1, 0), (1, 1)])
spiece = TetrinosPieces('spiece', [(1, 0), (1, 1), (0, 1), (0, 2)])
tpiece = TetrinosPieces('tpiece', [(0, 1), (1, 0), (1, 1), (1, 2)])
zpiece = TetrinosPieces('zpiece', [(0, 0), (0, 1), (1, 1), (1, 2)])

# Add all pieces to a list
allTetrinoPieces = [ipiece, jpiece, lpiece, opiece, spiece, tpiece, zpiece]


TetrinoColors = ['red', 'green', 'yellow', 'blue']

#returns a random selection of a tetrino piece and a random tetrino color in a tuple
def getNextPiece(app):
    return (random.choice(allTetrinoPieces), random.choice(TetrinoColors))

