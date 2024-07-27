import random

#check if the next position of the block is valid and legal
def isOnBoardAndValid(app, nextRow, nextCol):
    if nextRow >= app.rows or nextCol < 0 or nextCol >= app.cols or (nextRow, nextCol) in app.board:
        return False
    return True

#move each sand particle down
def moveSandsDown(app):
    #establishing directions and positions to remove once inside the for loop
    direction = [(1, -1), (1, +1)]
    valuesToRemove = set()
    valuesToAdd = set()

    #looping through each coordinate of sand and go down one if the spot below is empty
    for row, col in app.board:
        color = app.board.get((row, col))
        if isOnBoardAndValid(app, row+1, col):
            #add the values to a set to remove it after the loop
            #also add the new value to another set to add it after the loop
            valuesToRemove.add((row, col))
            valuesToAdd.add((row+1, col, color))
        else:
            #samething but to leftbottom and rightbottom directions if direct bottom is filled
            drow, dcol = random.choice(direction)
            newRow = drow + row
            newCol = dcol + col
            if isOnBoardAndValid(app, newRow, newCol):
                valuesToAdd.add((newRow, newCol, app.board[(row, col)]))
                valuesToRemove.add((row, col))
    
    #change if sand is moving; if it is we will change it later when adding new values 
    #if not changed later, it will remain false
    app.isSandMoving = False
    #add values to dictionary from set
    for keys in valuesToAdd:
        lrow, rcol, rcolor = keys
        app.board[(lrow, rcol)] = rcolor
        #change to show that sand is moving
        app.isSandMoving = True

    #removing values to dictionary from set
    for keys in valuesToRemove:
        lrow, lcol = keys
        app.board.pop((lrow, lcol))

def moveTetrinosDown(app):
    pass