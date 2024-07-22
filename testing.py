import copy
def solveMiniSudoku(board):
    newBoard = copy.deepcopy(board)
    return solveMiniSudokuHelper(newBoard)

def solveMiniSudokuHelper(board):
    x = findEmptyCell(board)
    if x == None:
        return board
    else:
        row, col = x
        validNum = [1, 2, 3, 4]
        for num in validNum:
            board[row][col] = num
            if isValidBoard(board):
                result = solveMiniSudokuHelper(board)
                if result == None:
                    board[row][col] = 0
                else:
                    return result
            else:
                board[row][col] = 0
        
    return None
    

# def isValidMove(board, row, col, num):
#     board = copy.deepcopy(board)
#     if board[row][col] != 0:
#         return False
#     else:
#         board[row][col] = num
#         return isValidBoard(board)
    
# def isCompletedBoard(board):
#     for i in board:
#         for j in i:
#             if j == 0:
#                 return False
#     return True

def isValidBoard(board):
    for row in range(len(board)):
        if not checkRow(board, row):
            return False
    for col in range(len(board[0])):
        if not checkCol(board, col):
            return False
    if not checkQuads(board):
        return False
    return True

def checkQuads(board):

    quads = []
    for bigRow in range(0, len(board), 2):
        for bigCol in range(0, len(board[0]), 2):
            currentQuad = []
            currentQuad.append(board[bigRow][bigCol])
            currentQuad.append(board[bigRow][bigCol+1])
            currentQuad.append(board[bigRow+1][bigCol])
            currentQuad.append(board[bigRow+1][bigCol+1])
            quads.append(currentQuad)
        
        
    quadNum = set()
    for i in quads:
        quadNum = {1, 2, 3, 4}
        for j in i:
            if j in quadNum:
                quadNum.remove(j)
            elif j == 0:
                pass
            else:
                return False
    return True


def checkRow(board, row):
    rowNum = {1, 2, 3, 4}
    for i in board[row]:
        if i in rowNum:
            rowNum.remove(i)
        elif i == 0:
            pass
        else:
            return False
    return True


def checkCol(board, col):
    colNum = {1, 2, 3, 4}
    for i in range(len(board)):
        j = board[i][col]
        if j in colNum:
            colNum.remove(j)
        elif j == 0:
            pass
        else:
            return False
    return True
        
        
def findEmptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


def testSolveMiniSudoku():
    board1  = [[3, 0, 0, 0],
               [0, 1, 0, 3],
               [4, 0, 1, 0],
               [0, 0, 0, 0]]
    solved1 = [[3, 4, 2, 1],
               [2, 1, 4, 3],
               [4, 3, 1, 2],
               [1, 2, 3, 4]]
    board1Copy = copy.deepcopy(board1)
    assert(solveMiniSudoku(board1) == solved1)
    assert(board1 == board1Copy) # verify we do not mutate the original board

    board2  = [[4, 0, 0, 2],
               [0, 2, 0, 0],
               [0, 0, 3, 0],
               [0, 0, 0, 1]]
    solved2 = [[4, 3, 1, 2],
               [1, 2, 4, 3],
               [2, 1, 3, 4],
               [3, 4, 2, 1]]
    board2Copy = copy.deepcopy(board2)
    assert(solveMiniSudoku(board2) == solved2)
    assert(board2 == board2Copy) # verify we do not mutate the original board

    board3  = [[0, 3, 0, 0],
               [0, 0, 0, 3],
               [1, 0, 0, 0],
               [0, 0, 4, 0]]
    solved3 = [[2, 3, 1, 4],
               [4, 1, 2, 3], 
               [1, 4, 3, 2], 
               [3, 2, 4, 1]]
    board3Copy = copy.deepcopy(board3)
    assert(solveMiniSudoku(board3) == solved3)
    assert(board3 == board3Copy) # verify we do not mutate the original board
    
    board4 = [[4, 3, 0, 0], # This board has no solution
              [1, 0, 3, 0],
              [0, 0, 2, 0],
              [4, 1, 0, 1]]
    board4Copy = copy.deepcopy(board4)
    assert(solveMiniSudoku(board4) == None)
    assert(board4 == board4Copy) # verify we do not mutate the original board

def main():
    testSolveMiniSudoku()

main()
