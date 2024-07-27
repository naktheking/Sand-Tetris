import random

class TetrinosPieces():
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
    
        
allTetrinoPieces = {
    #coordinate value of all tetrino pieces with (0, 0) at left-top
    'i-piece': [(0, 0), (0, 1), (0, 2), (0, 3)],
    'j-piece': [(0, 0), (1, 0), (1, 1), (1, 2)],
    'l-piece': [(1, 0), (1, 1), (1, 2), (0, 2)],
    'o-piece': [(0, 0), (0, 1), (1, 0), (1, 1)],    
    's-piece': [(1, 0), (1, 1), (0, 1), (0, 2)],
    't-piece': [(0, 1), (1, 0), (1, 1), (1, 2)],
    'z-piece': [(0, 0), (0, 1), (1, 1), (1, 2)]
}

TetrinoColors = ['red', 'green', 'yellow', 'blue']

#returns a random selection of a tetrino piece and a random tetrino color in a tuple
def getNextPiece(app):
    return (random.choice(allTetrinoPieces.keys()), random.choice(TetrinoColors))

