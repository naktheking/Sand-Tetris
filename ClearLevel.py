def findAllColorGroupOnLeft(app):
    allPixelColorOnLeft = {}
    for i in range(app.rows-1, -1, -1):
        if (i,0) not in app.board:
            break
        else:
            currentColor = app.board[(i, 0)]
        if currentColor == None:
            break
        else:
            if (i-1, 0) in app.board and app.board[(i-1, 0)] == currentColor:
                continue
            else:
                allPixelColorOnLeft[i] = currentColor

    #returns a dictionary of the top of the color groups on the left side
    #key: row     value: color
    print(allPixelColorOnLeft.keys(), allPixelColorOnLeft.values())
    return allPixelColorOnLeft 

def checkLevelConnected(app):
    pass

